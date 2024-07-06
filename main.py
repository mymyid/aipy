import functions_framework
from flask import jsonify
from module import botReply

@functions_framework.http
def chat(request):
    data = request.get_json(silent=True)
    message = data.get('message', '')
    message = message.replace('iteung', '').replace('teung', '')
    
    if not message:
        return jsonify({'status': "true", 'message': ""})

    message, status = botReply(message)
    return jsonify({'status': status, 'message': message})

