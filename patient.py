from sqlalchemy import Column, Integer, String
from base import Base


# when this class is contructed, all Column objects are replaced with Python accessors 'descriptors'
class Patient(Base):
    __tablename__ = 'paitents'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))                  # Strings require a length in mysql
    number = Column(String(100))


    def __repr__(self):
        return "<Patient(name='%s', number='%s'" % (self.name, self.number)

    # __init__ (default constructor) is provided by Declarative
    # the constructor will accept any of the columns as keywords