import json

def action_form(request):
  payload = request.get_json()
  print("action_form received request:", payload)
  
  form = [
    {
      "name": "request_label", 
      "label": "Request Label",
      "description": "Defaults to report name if left blank", 
      "type": "string", 
      "required": False, 
      "sensitive": True
    },
    {
      "name": "request_type", 
      "label": "Select Request Type", 
      "type":"select",
      "required": True, 
      "sensitive": False, 
      "options": [
        {
          "name": "images",
          "label": "Send Link to Image Collection"
        },
        {
          "name": "approval_only", 
          "label": "Send Request for Manual Approval"
        },
      ]
    }
  ]

  return json.dumps(form)
