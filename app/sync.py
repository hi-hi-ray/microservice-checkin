import json
import boto3


def send_to_sqs(id, type_stop, id_stop, type_alert, timestamp=None):
    client = boto3.resource('sqs', region_name='sa-east-1',
                            aws_access_key_id="AKIAWJLET7HYW67KFCPO",
                            aws_secret_access_key="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",
                            endpoint_url='https://sqs.sa-east-1.amazonaws.com/432392108529')
    # data = {'id': id, 'type_stop': type_stop, 'id_stop': id_stop, 'type_alert': type_alert, 'timestamp': timestamp}
    queue_name = 'tickers'
    queue = client.get_queue_by_name(QueueName=queue_name)

    message = 'The ticker {0} at {1} in the stop {2} with id {3} had his {4} maded'.format(id, timestamp,
                                                                                 type_stop, id_stop, type_alert)
    #
    # response = queue.send_message(
    #     MessageBody=message
    # )

    response = queue.send_messages(Entries=[
        {
            'Id': '1',
            'MessageBody': 'world'
        },
        {
            'Id': '2',
            'MessageBody': 'boto3',
            'MessageAttributes': {
                'Author': {
                    'StringValue': 'Daniel',
                    'DataType': 'String'
                }
            }
        }
    ])

    print(response)


def get_from_sqs():
    client = boto3.resource('sqs', region_name='sa-east-1',
                            aws_access_key_id="AKIAWJLET7HYW67KFCPO",
                            aws_secret_access_key="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",
                            endpoint_url='https://sqs.sa-east-1.amazonaws.com/432392108529')
    # data = {'id': id, 'type_stop': type_stop, 'id_stop': id_stop, 'type_alert': type_alert, 'timestamp': timestamp}
    queue_url = 'https://sqs.sa-east-1.amazonaws.com/432392108529/tickers'

    response = client.receive_message(
        QueueUrl=queue_url,
        AttributeNames=[
            'SentTimestamp'
        ],
        MaxNumberOfMessages=1,
        MessageAttributeNames=[
            'All'
        ],
        VisibilityTimeout=0,
        WaitTimeSeconds=0
    )

    print(response)



