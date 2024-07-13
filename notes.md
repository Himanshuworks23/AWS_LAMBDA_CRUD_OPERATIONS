https://ddgcc2nm2i.execute-api.ap-south-1.amazonaws.com/diot


"""
def get_all_devices(event):
    all_devices = []
    list_devices = s3.list_objects_v2(Bucket=BUCKET_NAME)
    devices = list_devices.get('Contents', [])
    for device in devices:
        device_id = device["Key"]
        try:
            get_device_details = s3.get_object(
                Bucket=BUCKET_NAME,
                Key=str(device_id)
            )
            device_data = get_device_details['Body'].read().decode('utf-8')
            all_devices.append(json.loads(device_data))

        except Exception as e:
            print(f'Error fetching with device_id: {device_id} : {str(e)}')
"""