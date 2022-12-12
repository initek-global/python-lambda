import json


def lambda_handler(event, context):
    body = json.loads(event['body'])

    print('###################### BODY ######################')
    print(body)

    return {
        'statusCode': 200,
        'body': json.dumps(body)
    }