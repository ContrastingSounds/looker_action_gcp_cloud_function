import json
import looker_sdk


def action_execute(request):
    payload = request.get_json()
    print('action_execute payload:', payload)
    keys = ['type', 'scheduled_plan', 'attachment', 'data', 'form_params']
    for key in keys:
        print(key, ':', payload[key])

    original_query = payload['scheduled_plan']['query']
    print('query details:', original_query)

    sdk = looker_sdk.init31()

    modified_query = {
        "view": "order_items",
        "fields": ["order_items.user_id"] + original_query['fields'],
        "filters": {
            "order_items.created_date": "2021/01/01 to 2021/03/30"
        },
        "sorts": [
            "order_items.created_date desc"
        ],
        "limit": "10",
        "model": "hns_core",
    }
    resp = sdk.run_inline_query("json", modified_query)
    resp = json.loads(resp)
    print('response to modified query:', resp)
    
    return {
        'statusCode': 200,
        'body': json.dumps('action_execute received')
    }
