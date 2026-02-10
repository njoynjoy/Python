import boto3
# Create an S3 client
client = boto3.client('s3')
# List all bucketsresponse = s3.list_buckets()
# Print the bucket names
response = client.create_bucket(Bucket='njoy-test-bucket')