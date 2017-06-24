import os

import schedule
import time

from cwb.api.fd0047 import FD0047
from cwb.data.destination.task import TaskService
from daemon import Daemon


class SetUp:
    def __init__(self):
        self.every_day_at = None
        self.cwb_authorization = None

    def set_every_day_at(self, every_day_at):
        self.every_day_at = every_day_at

    def set_cwb_authorization(self, cwb_authorization):
        self.cwb_authorization = cwb_authorization


class CWBDaemon(Daemon):
    def __job(self, authorization):
        api = FD0047(authorization, "001", location_name="頭城鎮")
        data_set = api.get_data_set()
        return TaskService.set_task(data_set)

    def __get_conf(self):
        set_up = SetUp()

        if os.path.isfile("..\setup.conf"):
            file = open("..\setup.conf", "r")

            line = file.readline()
            while line:
                print(line)
                line = file.readline()

                if line.startswith("EveryDayAt"):
                    set_up.every_day_at = line.replace("EveryDayAt", "").strip()
                elif line.startswith("CWBAuthorization"):
                    set_up.cwb_authorization = line.replace("CWBAuthorization", "").strip()

            file.close()
        else:
            print("lost setup.conf file.")

        return set_up

    def run(self):
        set_up = self.__get_conf()
        schedule.every().day.at(set_up.every_day_at).do(self.__job, [set_up.cwb_authorization])
        while True:
            schedule.run_pending()
            time.sleep(1)
