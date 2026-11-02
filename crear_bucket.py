import boto3
from botocore.exceptions import ClientError
from helpers import body_de, respuesta

def lambda_handler(event, context):
    try:
        nombre = body_de(event)['bucket']
        if not isinstance(nombre, str) or not 3 <= len(nombre) <= 63:
            raise ValueError('Nombre de bucket invalido')
        boto3.client('s3', region_name='us-east-1').create_bucket(Bucket=nombre)
        return respuesta(200, mensaje='Bucket creado', bucket=nombre)
    except (ValueError, KeyError, ClientError) as e:
        return respuesta(400, error=str(e))
