from sys import prefix

import boto3
s3 = boto3.client('s3')

files = s3.list_objects_v2(Bucket='cap1after', Prefix = '')
# print(files['Contents'])
a=[]
for i in files['Contents']:
    if i['Key'].endswith('.csv') and i['Key'].startswith('ops'):
        a.append(i['Key'])

print(a)