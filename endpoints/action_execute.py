import json
import looker_sdk

def action_execute(request):
    payload = request.get_json()
    print('action_execute received request:', payload)

    sdk = looker_sdk.init31()
    me = sdk.me()
    print('sdk.user()', me)
    
    return {
        'statusCode': 200,
        'body': json.dumps('action_execute received')
    }
