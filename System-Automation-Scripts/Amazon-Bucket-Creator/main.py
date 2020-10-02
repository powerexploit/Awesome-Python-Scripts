#!/bin/python3

import boto3
from botocore.exceptions import ClientError
from defaults import AMAZON_SECRETS


client = boto3.client(AMAZON_SECRETS.get('service'),
                      aws_access_key_id=AMAZON_SECRETS.get('aws_access_key_id_value'),
                      aws_secret_access_key=AMAZON_SECRETS.get('aws_secret_access_key_value'))

try:
    bucket = client.create_bucket(Bucket=AMAZON_SECRETS.get('bucket_value'),
                                  CreateBucketConfiguration={
                                      'LocationConstraint': AMAZON_SECRETS.get('location_constraint_value')
                                  })
except ClientError as error:
    print(f'[-] Error: {error}')
else:
    print(f'[+] {AMAZON_SECRETS.get("bucket_value")} successfully created!')
    print(f'[+] Location: {bucket.get("Location")}')
