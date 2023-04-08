import json
from gpt_service import ChatGptService
from gpt_model import MessageRequestDTO
# import requests
 
def get_ai_answer(data:dict):
    return ChatGptService.get_ai_model_answer(MessageRequestDTO.new_instance_from_flask_body(data))

def list_models():
    return ChatGptService.list_models()

def lambda_handler(event, context):
    print('event >>',event)
    print('context >>',context)
   
    #     raise e

    if event['httpMethod'] == 'POST':
        body = event.get('body')  # get the value of 'body' key from event
        if body:
            try:
                body = json.loads(body)
            except ValueError:
                return {
                    "statusCode": 400,
                    "body": json.dumps({
                        "error": "Invalid JSON in request body",
                    }),
                }

            return {
                "statusCode": 200,
                "body": json.dumps({
                    "version": 3,
                    "message": get_ai_answer(body),

                }),
            }
        else:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "error": "Request body is empty",
                }),
            }
        
    #    ### if 'body' not in event:
    #         return {
    #             "statusCode": 400,
    #             "body": json.dumps({
    #                 "version": 3,
    #                 "result": {
    #                     "err": "Empty body,Found !!"
    #                 },
    #             }),
    #         } ###

    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "version": 3,
            "message": list_models(),
            
        }),
    }
