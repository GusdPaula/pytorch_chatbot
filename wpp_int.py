from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from chat import chat_response

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    user_msg = request.values.get('Body', '').lower()
    bot_resp = MessagingResponse()
    msg = bot_resp.message()

    response = chat_response(user_msg)

    msg.body(response)

    return str(bot_resp)


if __name__ == '__main__':
    app.run(debug=True)
