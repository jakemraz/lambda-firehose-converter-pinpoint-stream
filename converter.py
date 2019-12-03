import json


def convert(payload):
    ret = {}
    
    if payload['event_type'] != '_campaign.opened_notification':
        return ret
    
    valid_properties = [
        'event_type',
        'event_timestamp',
        'arrival_timestamp',
        'application',
        'client',
        'attributes'
    ]

    for prop in valid_properties:
        ret[prop] = payload[prop]
    
    return ret


