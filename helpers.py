import json

def body_de(event):
    body = event.get('body', event)
    if isinstance(body, str):
        body = json.loads(body)
    if not isinstance(body, dict):
        raise ValueError('El cuerpo debe ser un JSON')
    return body

def respuesta(status, **data):
    return {'statusCode': status, **data}
