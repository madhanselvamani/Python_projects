from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import requests
import os

app = Flask(__name__)

# Your Twilio credentials
account_sid = "TWILIO_ACCOUNT_SID"
auth_token = 'TWILIO_AUTH_TOKEN'
client = Client(account_sid, auth_token)

# Your Merriam-Webster API Key
API_KEY = 'MERRIAM_WEBSTER_API_KEY'
# Merriam-Webster API URL
URL = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'

def get_word_meaning(word):
    response = requests.get(URL + word, params={'key': API_KEY})
    if response.status_code == 200:
        data = response.json()
        if data and isinstance(data[0], dict) and 'shortdef' in data[0]:
            return '\n'.join(data[0]['shortdef'])
    return 'No definition found.'

@app.route('/whatsapp', methods=['POST'])
def whatsapp():
    incoming_msg = request.values.get('Body', '').strip()
    resp = MessagingResponse()
    msg = resp.message()

    if incoming_msg:
        meaning = get_word_meaning(incoming_msg)
        msg.body(f"Meaning of '{incoming_msg}':\n{meaning}")
    else:
        msg.body("Please send a word to get its meaning.")

    return str(resp)

if __name__ == '__main__':
    app.run(debug=True, port=4040)
