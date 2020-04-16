import boto3


def add_to_sqs(id, timestamp, type_stop, id_stop, type_alert):
    sqs = boto3.client('sqs')
    sqs_address = 'https://sqs.sa-east-1.amazonaws.com/432392108529/tickers'
    response = sqs.send_message(
        QueueUrl=sqs_address,
        MessageAttributes={
            'id': {
                'DataType': 'Integer',
                'StringValue': id
            },
            'timestamp': {
                'DataType': 'String',
                'StringValue': timestamp
            },
            'type_stop': {
                'DataType': 'String',
                'StringValue': type_stop
            },
            'id_stop': {
                'DataType': 'String',
                'StringValue': id_stop
            },
            'type_alert': {
                'DataType': 'String',
                'StringValue': type_alert
            }
        },
        MessageBody=(
            'The ticker {0} at {1} in the stop {2} with id {3} was {4}'.format(id, timestamp,
                                                                               type_stop, id_stop, type_alert)
        )
    )

