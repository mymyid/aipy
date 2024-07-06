from blacksheep import Application, FromJSON
from module import botReply

app = Application()

@app.route('/chat', methods=['POST'])
async def chat(data: FromJSON[dict]):
    message = data.get('message', '')
    message = message.replace('iteung', '').replace('teung', '')
    if not message:
        return {'status': "true", 'message': ""}

    message, status = botReply(message)
    return {'status': status, 'message': message}

if __name__ == "__main__":
    app.start()
