from sqlalchemy import Column, Integer, String
from base import Base

# when this class is contructed, all Column objects are replaced with Python accessors 'descriptors'
class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    message = Column(String(300))                  # Strings require a length in mysql
    paitentID = Column(Integer)


    def __repr__(self):
        return "<Patient(name='%s', number='%s'" % (self.name, self.number)

    # __init__ (default constructor) is provided by Declarative
    # the constructor will accept any of the columns as keywords
