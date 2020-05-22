from sqlalchemy import Column, Integer, String
from base import Base

# when this class is contructed, all Column objects are replaced with Python accessors 'descriptors'
class Quote(Base):
    __tablename__ = 'quotes'

    id = Column(Integer, primary_key=True)
    quote = Column(String(300))                  # Strings require a length in mysql
    category = Column(String(100))



    def __repr__(self):
        return "<Quote(quote='%s', category='%s'" % (self.quote, self.category)
    # __init__ (default constructor) is provided by Declarative
    # the constructor will accept any of the columns as keywords