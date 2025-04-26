from boto3 import Session
client= Sessoion(
    **dbutils.credentials.getCurrentCredentials(),
    region_name=spa
)