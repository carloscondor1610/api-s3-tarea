import base64
import binascii
import boto3
from botocore.exceptions import ClientError
from helpers import body_de, respuesta

def lambda_handler(event, context):
    try:
        body = body_de(event)
        bucket = body['bucket']
        directorio = body['directorio'].strip('/')
        archivo = body['archivo']
        contenido = base64.b64decode(body['contenido_base64'], validate=True)
        if not directorio or not archivo or '/' in archivo or '\\' in archivo or archivo in ('.', '..') or '..' in directorio.split('/'):
            raise ValueError('Ruta invalida')
        key = directorio + '/' + archivo
        boto3.client('s3').put_object(Bucket=bucket, Key=key, Body=contenido, ContentType=body.get('content_type','application/octet-stream'))
        return respuesta(200, mensaje='Archivo subido', bucket=bucket, archivo=key, bytes=len(contenido))
    except (KeyError, ValueError, AttributeError, binascii.Error, ClientError) as e:
        return respuesta(400, error=str(e))
