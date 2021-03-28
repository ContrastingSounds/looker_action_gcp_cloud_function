import json

print('Loading action_execute function')

def action_execute(event, context):
    print('action_form received event of type:', type(event))
    print('event keys:', event.keys())
    print('event body:', event['body'])
    
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('action_execute received')
    }
