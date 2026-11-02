import boto3
from botocore.exceptions import ClientError
from helpers import body_de, respuesta

def lambda_handler(event, context):
    try:
        body = body_de(event)
        bucket = body['bucket']
        directorio = body['directorio'].strip('/')
        if not directorio or '..' in directorio.split('/'):
            raise ValueError('Directorio invalido')
        key = directorio + '/'
        boto3.client('s3').put_object(Bucket=bucket, Key=key, Body=b'')
        return respuesta(200, mensaje='Directorio creado', bucket=bucket, directorio=key)
    except (ValueError, KeyError, AttributeError, ClientError) as e:
        return respuesta(400, error=str(e))
