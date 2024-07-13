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
    elif http_method == "GET":
        return get_device(event)
    else:
        return{
            'statusCode' : 201,
            'body' : json.dumps("Work in progress")
        }
    
    
    
    
def create_device(event):
    payload = json.loads(event['body']) #.loads create any string to dictionary format (json to python)
    device_id = payload['device_id']
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=str(device_id),
        #Key=str(device_id)+"_"+str(time.time())+".json",
        Body = json.dumps(payload) #.dumps converts any python object into json
    )
    return{
        'statusCode' : 201,
        'body' : json.dumps("Device created Successfully")
    }
    

def get_device(event):
    
    device_id = event['queryStringParameters']['device_id']
    try:
        get_device_details= s3.get_object(
            BUCKET=BUCKET_NAME,
            Key=str(device_id)
        )
        device_data=get_device_details['Body'].read().decode('utf-8')
        return{
            'statusCode' : 200,
            'body' : device_data
        }
        
    except s3.exceptions.NoSuchKey as e:
        print(f"{device_id} doesn't exist")
        return{
            "statusCode":404,
            'body':json.dumps("Device ID not found")
        }

def get_all_devices(event):
    pass

def update_device(event):
    pass

def delete_device(event):
    pass