from datetime import datetime
from sqlalchemy.orm import sessionmaker

from cwb.data.destination import database
from cwb.data.destination.database import Task


class TaskService:
    @staticmethod
    def set_task(data_set):
        Session = sessionmaker(bind=database.engine)
        session = Session()

        task = Task()
        task.crawl_time = datetime.now()
        task.description = data_set.Contents.content_description
        session.add(task)

        for locations in data_set.locations_list:
            for location in locations.location_list:


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
