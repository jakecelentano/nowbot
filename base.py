from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
import secrets

print('Start base')
Base = declarative_base()

connection_string = 'mysql+pymysql://{0}:{1}@{2}/{3}'.format(secrets.dbuser, secrets.dbpass, secrets.dbhost, secrets.dbname)

# the engine is source of database connectivity
engine = create_engine(connection_string, pool_size=30, max_overflow=10, echo=True)

from quote import Quote
from message import Message
from patient import Patient

Base.metadata.create_all(engine)


# Our defined Session class will serve as a factory for new Session objects
Session = sessionmaker(bind=engine)


