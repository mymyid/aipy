import functions_framework
from json import dumps
from module import botReply

@functions_framework.http
def chat(request):
    data = request.get_json(silent=True)
    message = data.get('message', '')
    message = message.replace('iteung', '').replace('teung', '')
    
    if not message:
        return dumps({'status': "true", 'message': ""})

    message, status = botReply(message)
    return dumps({'status': status, 'message': message})

