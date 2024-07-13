import json
import boto3
import os
import time

s3 = boto3.client("s3")
BUCKET_NAME = os.environ['BUCKET_NAME']
def lambda_handler(event,context):
    print(event)
    http_method = event['httpMethod']
    if http_method == "POST":
        return create_device(event)
    else:
        return{
            'statusCode' : 201,
            'body' : json.dumps("Work in progress")
        }
    
    
    
    
def create_device(event):
    payload = json.loads(event['body'])
    device_id = payload['device_id']
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=str(device_id)+"_"+str(time.time())+".json",
        Body = json.dumps(payload) 
    )
    return{
        'statusCode' : 201,
        'body' : json.dumps("Device created Successfully")
    }
    pass

def get_device(event):
    pass

def get_all_devices(event):
    pass

def update_device(event):
    pass

def delete_device(event):
    pass