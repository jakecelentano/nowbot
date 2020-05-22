from base import Base

def main():
    from quote import Quote
    from message import Message
    from patient import Patient

    Base.metadata.create_all(engine)

