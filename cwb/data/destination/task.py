from datetime import datetime

import sqlalchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker


class TaskService:
    @staticmethod
    def set_task(data_set):
        engine = create_engine("mysql+pymysql://root:123456@localhost/lighthouse", encoding='utf-8', echo=True)
        metada = MetaData(bind=engine)

        Session = sessionmaker(bind=engine)
        session = Session()

        Task = sqlalchemy.Table("task", metada, autoload=True)
        task = Task()
        task.crawl_time = datetime.now()
        session.add(task)

        row = session.query(Task).first()
        if row:
            print("Found data")
            print(row)
        else:
            print("Can't find data")

        session.rollback()

        row = session.query(Task).first()
        if row:
            print("Found data after rollback")
            print(row)
        else:
            print("Can't find data after rollback")

        session.commit()
