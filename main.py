import functions_framework
from json import dumps
from module import botReply

@functions_framework.http
def chat(request):
    request_json = request.get_json(silent=True)
    request_args = request.args
    if request_json and "message" in request_json:
        message = request_json["message"]
    elif request_args and "name" in request_args:
        message = request_args["message"]
    else:
        message = ""

    message = message.replace('iteung', '').replace('teung', '')
    
    if not message:
        return dumps({'status': "true", 'message': ""})

    message, status = botReply(message)
    return dumps({'status': status, 'message': message})

