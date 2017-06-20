# https://godleon.github.io/blog/2015/01/10/sqlalchemy-core-study-notes
# https://faithincode.tech/2016/09/28/python-sqlalchemy-orm-2/
# https://www.sqlalchemy.org/library.html#tutorials
# http://pythoncentral.io/introductory-tutorial-python-sqlalchemy/
import hashlib
import unittest

# import pymysql
import sqlalchemy
# from alembic import op
from sqlalchemy import Column, String, Integer, create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from cwb.api.fd0047 import FD0047
from cwb.data.destination.task import TaskService

# Base = declarative_base()


# class User(Base):
#     __tablename__ = 'users'
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String(16))
#     username = Column(String(32))
#     password = Column(String(16))
#
#     def __init__(self, name, username, password):
#         self.name = name
#         self.username = username
#         self.password = hashlib.sha1(password).hexdigest()
#
#     def __repr__(self):
#         return "User('{}','{}', '{}')".format(self.name, self.username, self.password)


class TestSQLAlchemy(unittest.TestCase):
    # def test_create_table(self):
    #     engine = create_engine("mysql+pymysql://root:123456@localhost/test", encoding='utf-8', echo=True)
    #     Base.metadata.create_all(engine)
    #     auser = User('user1', 'username', 'userpassword'.encode('utf-8'))
    #     print('Mapper:', auser.__mapper__)

    # def test_session(self):
    #     engine = create_engine("mysql+pymysql://root:123456@localhost/test", encoding='utf-8', echo=True)
    #     Base.metadata.create_all(engine)
    #
    #     Session = sessionmaker(bind=engine)
    #     session = Session()
    #
    #     user_1 = User('user1', 'username1', 'password_1'.encode('utf-8'))
    #     session.add(user_1)
    #
    #     row = session.query(User).filter_by(name='user1').first()
    #     if row:
    #         print("Found user1")
    #         print(row)
    #     else:
    #         print("Can't find user1")
    #
    #     session.rollback()
    #
    #     row = session.query(User).filter_by(name='user1').first()
    #     if row:
    #         print("Found user1 after rollback")
    #         print(row)
    #     else:
    #         print("Can't find user1 after rollback")
    #
    #     user_2 = User('user2', 'username2', 'password_2'.encode('utf-8'))
    #     session.add(user_2)
    #     session.commit()

    # def test_query(self):
    #     engine = create_engine("mysql+pymysql://root:123456@localhost/test", encoding='utf-8', echo=True)
    #     # Base.metadata.create_all(engine)
    #
    #     Session = sessionmaker(bind=engine)
    #     session = Session()
    #
    #     rows = session.query(User).from_statement('SELECT * FROM users WHERE name=:name').params(name='user1')
    #     for r in rows:
    #         print(r.id)

    # def test_alembic(self):
    #     engine = create_engine("mysql+pymysql://root:123456@localhost/lighthouse", encoding='utf-8', echo=True)
    #     metada = MetaData(bind=engine)
    #
    #     tasks = sqlalchemy.Table("task", metada, autoload=True)
    #     print(len(tasks))

    def test_task(self):
        api = FD0047("CWB-C9C20F8C-2237-46EB-B015-C52E09A8BDDB", "001", location_name="頭城鎮")
        data_set = api.get_data_set()
        TaskService.set_task(data_set)
