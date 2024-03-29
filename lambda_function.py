import converter
import json
import jhb_b64 as b64

def lambda_handler(event, context):
    output = []
    
    for record in event['records']:

        payload = json.loads(b64.decode_utf8(record['data']))
        
        # convert here
        converted = converter.convert(payload)
        result = 'Ok'
        if bool(converted) is False:
            result = 'Dropped'

        out_record = {
            'recordId': record['recordId'],
            'result': result,
            'data': b64.encode_utf8(json.dumps(converted))
        }
        output.append(out_record)
    return {'records': output}
    