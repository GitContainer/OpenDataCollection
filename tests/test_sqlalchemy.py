import hashlib
import unittest

from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(16))
    username = Column(String(32))
    password = Column(String(16))

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = hashlib.sha1(password).hexdigest()

    def __repr__(self):
        return "User('{}','{}', '{}')".format(
            self.name,
            self.username,
            self.password
        )


class TestSQLAlchemy(unittest.TestCase):
    def test_create_table(self):
        engine = create_engine("mysql+pymysql://root:123456@localhost/test", encoding='utf-8', echo=True)
        Base.metadata.create_all(engine)
        auser = User('user1', 'username', 'userpassword'.encode('utf-8'))
        print('Mapper:', auser.__mapper__)
