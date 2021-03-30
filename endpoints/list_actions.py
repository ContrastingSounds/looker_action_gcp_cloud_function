from icon import icon_data_uri

def list_actions(request):
    payload = request.get_json()
    print("list_actions received request:", payload)
    
    actions_list = {
      "integrations": [
        {
          "name": "request_image_set",
          "label": "Request Image Set",
          "description": "Based on current query, generate a list of all images for research project.",
          "form_url": "https://us-central1-jeff-308116.cloudfunctions.net/action_form",
          "supported_action_types": ["query"],
          "supported_formats": ["json"],
          "url": "https://us-central1-jeff-308116.cloudfunctions.net/action_execute",
          "icon_data_uri": icon_data_uri,
          "params": [
            {
              "name": "example_param", 
              "label": "Example Param", 
              "required": False, 
              "sensitive": False
            }
          ],
          "supported_download_settings": ["url"]
        }
      ]
    }

    return actions_list
