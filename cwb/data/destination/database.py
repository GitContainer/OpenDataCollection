from sqlalchemy import create_engine, Table
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+pymysql://root:123456@localhost/lighthouse", encoding='utf-8', echo=True)
Base = declarative_base()


class Task(Base):
    __table__ = Table('task', Base.metadata, autoload=True, autoload_with=engine)


class Location(Base):
    __table__ = Table('location', Base.metadata, autoload=True, autoload_with=engine)


class WeatherElement(Base):
    __table__ = Table('weather_element', Base.metadata, autoload=True, autoload_with=engine)


class Time(Base):
    __table__ = Table('time', Base.metadata, autoload=True, autoload_with=engine)


class Parameter(Base):
    __table__ = Table('parameter', Base.metadata, autoload=True, autoload_with=engine)
