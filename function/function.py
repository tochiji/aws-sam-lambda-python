import json
import requests


def lambda_handler(event, context):
    print(requests.get('https://google.com'))
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
