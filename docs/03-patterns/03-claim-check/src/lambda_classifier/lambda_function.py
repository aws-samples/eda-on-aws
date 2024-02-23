import boto3
import json
import tempfile

s3_client = boto3.client('s3')
sqs_client = boto3.client('sqs')
dynamodb_client = boto3.client('dynamodb')

# Number of words to consider feedback as positive, negative or neutral
WORDS_THRESHOLD = 3

# DynamoDB Table to concentrate information about the feedback
DYNAMODB_TABLE = 'eda-feedback'

# Queues and their description to use them
queue_positive = {'description': 'positive', 'queue_name':'eda-feeling-good'}
queue_negative = {'description': 'negative', 'queue_name':'eda-feeling-negative'}
queue_neutral = {'description': 'neutral', 'queue_name':'eda-feeling-neutral'}

# Catalog of positive words to identify in feedback
catalog_good_words = [
    'good',
    'great',
    'awesome',
    'amazing',
    'excellent',
    'fantastic',
    'perfect',
    'nice',
    'cool',
    'wonderful'
]

# Catalog of negative words to identify in feedback
catalog_bad_words = [
    'bad',
    'terrible',
    'awful',
    'poor',
    'worst',
    'horrible',
    'boring',
    'lazy',
    'complex',
    'difficult'
]


# Entry point to process the event
def lambda_handler(event, context):
    print('Event:\n', json.dumps(event))

    # Get the reference of the event stored in S3
    bucket = event['detail']['bucket']
    object_key = event['detail']['key']
    stars = event['detail']['stars']

    response = s3_client.get_object(Bucket=bucket, Key=object_key)

    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(response['Body'].read())

    print(f'Object {object_key} retrieved from bucket {bucket}')

    with open(temp_file.name, 'r') as f:
        feedback = f.read()

    # Identify how many positive and negativew words are present in the feedback
    count_good_words = count_words(feedback, catalog_good_words)
    count_bad_words = count_words(feedback, catalog_bad_words)

    print(f'{count_good_words} good words and {count_bad_words} bad words')

    # Identity what queue to send the feedback for further processing
    if count_good_words >= WORDS_THRESHOLD or count_bad_words >= WORDS_THRESHOLD:
        if count_good_words > count_bad_words:
            queue_name = queue_positive['queue_name']
            feeling = queue_positive['description']
        elif count_good_words < count_bad_words:
            queue_name = queue_negative['queue_name']
            feeling = queue_negative['description']
        else:
            queue_name = queue_neutral['queue_name']
            feeling = queue_neutral['description']
    else:
        queue_name = queue_neutral['queue_name']
        feeling = queue_neutral['description']
    
    print(f'Queue {queue_name} identified')

    message = {
        'bucket': bucket,
        'key': object_key,
        'feeling': feeling,
        'stars': stars
    }
    
    # Send the message for further processing
    sqs_client.send_message(QueueUrl=queue_name, MessageBody=json.dumps(message))

    print(f'Message sent to queue {queue_name}')

    # Create or update the item in DynamoDB, the item can be present in the table and just be updated or it can be created directly
    # We use the reference from S3 to add the information about the feeling, no matter other processes have taken place
    dynamodb_client.update_item(
        TableName=DYNAMODB_TABLE,
        Key={
            'id': {
                'S': object_key
            }
        },
        ExpressionAttributeNames={
            '#B': 'bucket',
            '#QF': 'queue_feeling',
            '#F': 'feeling',
            '#S': 'stars'
        },
        ExpressionAttributeValues={
            ':b': {
                'S': bucket,
            },
            ':qf': {
                'S': queue_name,
            },
            ':f': {
                'S': str(feeling)
            },
            ':s': {
                'N': str(stars)
            }
        },
        UpdateExpression='SET #B = :b, #QF = :qf, #F = :f, #S = :s'
    )

    print(f'Item updated in table {DYNAMODB_TABLE}')

    return {
        'bucket': bucket,
        'key': object_key,
        'feeling' : feeling,
        'queueName': queue_name,
        'stars': stars,
        'dynamodbTable': DYNAMODB_TABLE
    }
        

# Function to count positive or negative word based on the catalogs
def count_words(text, catalog):
    count = 0
    text = text.replace('\n', '').replace('\r', '').replace('\t', '').replace('.', '').replace(',', '').replace('!', '')

    for word in text.split():
        if word in catalog:
            count += 1
    
    return count