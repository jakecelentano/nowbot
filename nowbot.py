from base import Session, engine, Base
from sqlalchemy import func, select
import random

class Nowbot:


    def getQuote(self, message):
        response = ""

        session = Session()
        from quote import Quote


        if message.lower() == 'hi':
            rand = random.randrange(0, session.query(Quote).filter(Quote.category == "greeting").count())
            response = session.query(Quote).filter(Quote.category == "greeting")[rand].quote
        else:
            rand = random.randrange(0, session.query(Quote).filter(Quote.category != "greeting").count())
            response = session.query(Quote).filter(Quote.category != "greeting")[rand].quote

        return response







