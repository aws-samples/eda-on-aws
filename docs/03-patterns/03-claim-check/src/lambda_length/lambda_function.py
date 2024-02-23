import boto3
import json
import tempfile

s3_client = boto3.client('s3')
sqs_client = boto3.client('sqs')
dynamodb_client = boto3.client('dynamodb')

# Queues catalog to define boundaries and queues to use
catalog_queues = [
    {'count_words_min': 0, 'count_words_max': 40, 'queue_name': 'eda-length-small'},
    {'count_words_min': 41, 'count_words_max': 99, 'queue_name': 'eda-length-medium'},
    {'count_words_min': 100, 'count_words_max': None, 'queue_name': 'eda-length-large'}
]

# DynamoDB Table to concentrate information about the feedback
DYNAMODB_TABLE = 'eda-feedback'


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
    
    # Count how many words are in the feedback
    feedback_count = len(feedback.split())

    # Identity what queue to send the feedback for further processing
    for queue in catalog_queues:
        if queue['count_words_max'] is not None:
            if feedback_count >= queue['count_words_min'] and feedback_count <= queue['count_words_max']:
                queue_name = queue['queue_name']
                break
        else:
            if feedback_count >= queue['count_words_min']:
                queue_name = queue['queue_name']
                break
    
    print(f'Queue {queue_name} identified')

    message = {
        'bucket': bucket,
        'key': object_key,
        'wordCount': feedback_count,
        'stars': stars
    }
    
    # Send the message for further processing
    sqs_client.send_message(QueueUrl=queue_name, MessageBody=json.dumps(message))

    print(f'Message sent to queue {queue_name}')

    # Create or update the item in DynamoDB, the item can be present in the table and just be updated or it can be created directly
    # We use the reference from S3 to add the information about word count, no matter other processes have taken place
    dynamodb_client.update_item(
        TableName=DYNAMODB_TABLE,
        Key={
            'id': {
                'S': object_key
            }
        },
        ExpressionAttributeNames={
            '#B': 'bucket',
            '#QL': 'queue_length',
            '#WC': 'word_count',
            '#S': 'stars'
        },
        ExpressionAttributeValues={
            ':b': {
                'S': bucket,
            },
            ':ql': {
                'S': queue_name,
            },
            ':wc': {
                'N': str(feedback_count)
            },
            ':s': {
                'N': str(stars)
            }
        },
        UpdateExpression='SET #B = :b, #QL = :ql, #WC = :wc, #S = :s'
    )

    print(f'Item updated in table {DYNAMODB_TABLE}')

    return {
        'bucket': bucket,
        'key': object_key,
        'wordCount' : feedback_count,
        'queueName': queue_name,
        'stars': stars,
        'dynamodbTable': DYNAMODB_TABLE
    }
