Lambda function code:

import json
import base64
import boto3
from datetime import datetime
import io
import http.client

def lambda_handler(event, context):
    s3_bucket_name = "medvision-lambda-api-upload"
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")
    s3 = boto3.client("s3")
    rekognition = boto3.client('rekognition')

    s3_object_key = f"content_{timestamp}.png"
    get_file_content = event["content"]
    decode_content = base64.b64decode(get_file_content)
    decode_content_str = decode_content.decode("utf-8")
    decoded_data = decode_content_str.split("data:image/png;base64,")[1].split(
        "------WebKitFormBoundary"
    )[0]

    decode_content_bytes = base64.b64decode(decoded_data)
    content_stream = io.BytesIO(decode_content_bytes)
    s3.upload_fileobj(
        Fileobj=content_stream, Bucket=s3_bucket_name, Key=s3_object_key
    )

    rekognition_response = rekognition.detect_labels(
        Image={"S3Object": {"Bucket": s3_bucket_name, "Name": s3_object_key}},
        MaxLabels=10, 
        MinConfidence=50,
    )

    response_items = []
    for label in rekognition_response["Labels"]:
        item = {
            "Name": label["Name"],
            "Confidence": label["Confidence"],
        }
        if "Medical" in label["Name"]:
            item["IsMedical"] = True
        if "Instances" in label and label["Instances"]:
            item["BoundingBox"] = label["Instances"][0]["BoundingBox"]
        response_items.append(item)

    print ("======== rekognition_response-start")
    print (json.dumps(response_items))
    print ("======== rekognition_response-end")
    

    data_to_send_str = json.dumps(response_items, indent=4)
    external_url = '01hegfw77cmkfhp4pbd0wfya8k00-4d2e4f58935400548e9d.requestinspector.com'
    headers = {'Content-Type': 'application/json'}
    conn = http.client.HTTPSConnection(external_url)
    conn.request("POST", "/", body=data_to_send_str, headers=headers)
    external_response = conn.getresponse()

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Headers": "Content-Type, Authorization",
            # "Access-Control-Allow-Origin": "https://medvision.s3.us-east-2.amazonaws.com",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE",
            "Access-Control-Allow-Credentials": True,
        },
        "body": json.dumps(response_items),
    }
