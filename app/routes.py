from app import app
from flask import request
from twilio.twiml.messaging_response import MessagingResponse
from twilio import twiml
from nowbot import Nowbot
from base import Session, engine, Base



@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message = request.form['Body']

    resp = MessagingResponse()

    dr = Nowbot()
    replyText = dr.getQuote(message)
    resp.message(replyText)

    return str(resp)



