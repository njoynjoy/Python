import boto3
import requests
# Create an S3 client
client = boto3.client('s3')

response = client.get_bucket_acl(
    Bucket='njoy-test-bucket'
)
#print(response)


for grant in response['Grants']:
    print(grant['Grantee'], grant['Permission'], grant['Grantee']['Type'], response['Owner']['ID'])
