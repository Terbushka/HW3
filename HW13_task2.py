import threading
from time import sleep
from datetime import datetime


class ActualTime(threading.Thread):
    def __init__(self, limit, name):
        threading.Thread.__init__(self)
        self.limit = limit
        self.name = name

    def run(self):
        for i in range(self.limit):
            print(f"Date and time: {datetime.now()} in {self.name}")
            sleep(2)


real_time1 = ActualTime(5,"Thread_1")
real_time2 = ActualTime(5,"Thread_2")

real_time1.start()
real_time2.start()

real_time1.join()
real_time2.join()
