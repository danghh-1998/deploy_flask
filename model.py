from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

from config import STRING_MAX_LENGTH, TEL_MAX_LENGTH, EMAIL_MAX_LENGTH

engine = create_engine('sqlite:///database.db', echo=True)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

Base = declarative_base()


def get_tels():
    return session.query(Tel)


def get_tel(name):
    return session.query(Tel).filter_by(name=name).first()


def create_tel(name, tel, email):
    session.add(Tel(name, tel, email))
    session.commit()


def update_tel(tel):
    session.query(Tel).filter_by(id=tel.id).update({'name': tel.name, 'tel_number': tel.tel_number, 'email': tel.email})
    session.commit()


def delete_tel(id_):
    session.delete(session.query(Tel).filter_by(id=id_).first())
    session.commit()


class Tel(Base):
    __tablename__ = 'tel_number'
    id = Column(type_=Integer, primary_key=True)
    name = Column(type_=String(length=STRING_MAX_LENGTH))
    tel_number = Column(type_=String(length=TEL_MAX_LENGTH), unique=True)
    email = Column(type_=String(length=EMAIL_MAX_LENGTH), unique=True)

    def __init__(self, name, tel_number, email):
        self.name = name
        self.tel_number = tel_number
        self.email = email


Base.metadata.create_all(bind=engine)
