import lambda_function

event = {
    "version": "0",
    "id": "5e6b5940-2435-8af1-31ac-2985af5b63f1",
    "detail-type": "Feedback sent",
    "source": "custom.feedback",
    "account": "852972878858",
    "time": "2024-01-28T22:32:01Z",
    "region": "us-east-1",
    "resources": [],
    "detail": {
        "bucket": "eda-claim-check",
        "key": "9994957fb10d421585cd1284cb2492ba"
    }
}

print(lambda_function.lambda_handler(event, None))