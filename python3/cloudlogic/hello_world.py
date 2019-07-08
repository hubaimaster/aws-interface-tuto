

def handler(payload, user):
    response = {
        'message': 'Hello world',
        'request_user': user,
        'payload_received': payload,
    }
    return response
