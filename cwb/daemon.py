import os

import schedule
import time

from cwb.api.fd0047 import FD0047
from cwb.data.destination.task import TaskService
from daemon import Daemon


class CWBDaemon(Daemon):
    def __job(self):
        api = FD0047("CWB-C9C20F8C-2237-46EB-B015-C52E09A8BDDB", "001", location_name="頭城鎮")
        data_set = api.get_data_set()
        return TaskService.set_task(data_set)

    def __get_conf(self):
        every_day_at = None

        if os.path.isfile("..\setup.conf"):
            file = open("..\setup.conf", "r")

            line = file.readline()
            while line:
                print(line)
                line = file.readline()

                if line.startswith("EveryDayAt"):
                    every_day_at = line.replace("EveryDayAt", "").strip()

            file.close()
        else:
            print("lost setup.conf file.")

        return every_day_at

    def run(self):
        every_day_at = self.__get_conf()
        schedule.every().day.at(every_day_at).do(self.__job())
        while True:
            schedule.run_pending()
            time.sleep(1)
