import json
import boto3
import os

HOSTED_ZONE_ID = os.environ['HOSTED_ZONE_ID']
USERNAME = os.environ['USERNAME']
PASSWORD = os.environ['PASSWORD']

def update_route53_record(hostname, ip):
    """Updates a Route53 record with the current IP address"""
    print(f"Updating Route53 record {hostname} for {HOSTED_ZONE_ID}")
    client = boto3.client('route53')
    response = client.change_resource_record_sets(
        ChangeBatch={
            'Changes': [
                {
                    'Action': 'UPSERT',
                    'ResourceRecordSet': {
                        'Name': hostname,
                        'ResourceRecords': [
                            {
                                'Value': ip,
                            },
                        ],
                        'TTL': 300,
                        'Type': 'A',
                    },
                },
            ],
            'Comment': 'Synology',
        },
        HostedZoneId=HOSTED_ZONE_ID,
    )
    print(response)

def ddns(event, context):
    """Handles the Lambda event"""
    if event['queryStringParameters']['username'] != USERNAME:
        print(f"Username does not match")
        return {"statusCode": 400, "body": "Unauthorized user"}
    if event['queryStringParameters']['password'] != PASSWORD:
        print(f"Password does not match")
        return {"statusCode": 400, "body": "Unauthorized password"}
    update_route53_record(event["queryStringParameters"]['hostname'], event["queryStringParameters"]['ip'])
    return {"statusCode": 200, "body": 'Record Set!'}
