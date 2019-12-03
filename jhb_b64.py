import base64

def decode_utf8(encoded_str):
    return base64.b64decode(encoded_str.encode('utf-8')).decode('utf-8')

def encode_utf8(plain_str):
    return base64.b64encode(plain_str.encode('utf-8')).decode('utf-8')
