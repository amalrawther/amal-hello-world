import json
import logging
import boto3

# Get the service client
BUCKET_NAME='dev-days-test'
KEY="hello.txt"
s3 = boto3.resource('s3')
logging.getLogger().setLevel(logging.INFO)
def lambda_handler(event, context):
    # TODO implement
    #any AWS Service other than
    logging.info(event)
    try:
        s3.Bucket(BUCKET_NAME).download_file(KEY, '/tmp/hello_world.txt')
    except botocore.exception.ClientError as e:
        if e.response['Error']['Code'] == '404':
            logging.error('Object not found')
        else:
            raise
    
    return {
        
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
