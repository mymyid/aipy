from flask import Flask, jsonify, request
from functions_framework import create_function

from module import botReply

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message', '')
    message = message.replace('iteung', '').replace('teung', '')
    
    if not message:
        return jsonify({'status': "true", 'message': ""})

    message, status = botReply(message)
    return jsonify({'status': status, 'message': message})

# Create a function that wraps the application
function = create_function(app)

# This part is required for local development
if __name__ == '__main__':
    function.run()
