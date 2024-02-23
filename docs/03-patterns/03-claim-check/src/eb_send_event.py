import boto3
import tempfile
import uuid
import json

s3_client = boto3.client('s3')
eb_client = boto3.client('events')

# Bucket to upload the feedback as an object
feedback_bucket = 'eda-claim-check'

# Function to send feedback as an object to S3 and send a reference as an event to EventBridge
def send_feedback(stars, message, bucket):
    if not message or not bucket or not message.split():
        return

    # Generate a unique reference/key
    object_id = uuid.uuid4().hex

    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(message.encode('utf-8'))

    s3_client.upload_file(temp_file.name, bucket, object_id)

    event_detail = {
        'stars': stars,
        'bucket': bucket,
        'key': object_id
    }

    response = eb_client.put_events(
        Entries=[
            {
                'Source': 'custom.feedback',
                'DetailType': 'Feedback sent',
                'Detail': json.dumps(event_detail)
            }
        ]
    )

    return response

# Sample positive feedback
feedback_good = '''I found this website to be absolutely amazing! The user experience was excellent from start to finish.
Navigation was a breeze thanks to the intuitive layout and clean design.
I was easily able to find exactly what I was looking for.
The content itself was fantastic - very well written, informative and helpful.
It was also really great how organized everything was into logical categories.
I was impressed by how quickly pages loaded too. Overall, this is an awesome, high quality site that delivers a truly amazing experience. Great work!
'''

# Sample negative feedback
feedback_negative = '''The website is very slow, I think this is a bad aspect because when I am in a hurry it's horrible to wait, not to mention it's boring. I also find difficult to browse through the site, I'd like to have a site map.
'''

# Sample neutral feedback
feedback_neutral = '''The website got the job done and provided the information I was looking for.
The layout and navigation were straightforward enough to find my way around.
Some sections could be organized more logically, but overall it was easy to browse.
The content covered the main topics but wasn't the most engaging to read.
It would be good to see some visuals added for variety.
Performance and load times were adequate.
While there isn't anything particularly impressive about the site, it serves its purpose in a satisfactory manner.
With some tweaks to content and design, the user experience could be improved.
'''

send_feedback(5, feedback_good, feedback_bucket)

send_feedback(1, feedback_negative, feedback_bucket)

send_feedback(3, feedback_neutral, feedback_bucket)
