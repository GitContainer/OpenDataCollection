from datetime import datetime
from sqlalchemy.orm import sessionmaker

from cwb.data.destination import database
from cwb.data.destination.database import Task
from cwb.data.destination.location import LocationService


class TaskService:
    @staticmethod
    def set_task(source):
        Session = sessionmaker(bind=database.engine)
        session = Session()

        task = Task()
        task.crawl_time = datetime.now()
        task.description = source.contents.content_description
        session.add(task)
        session.flush()

        all_success = True
        for locations in source.locations_list:
            for location in locations.location_list:
                if not LocationService.set_location(session, location, task.task_id):
                    all_success = False
                    break

        if all_success:
            session.commit()
            return True
        else:
            session.rollback()
            return False
