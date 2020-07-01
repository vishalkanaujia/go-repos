from random import seed
from random import randint
import sys

seed(1)

class RateLimit():
    def getTime(self, minute):
        if minute == 4:
            sys.exit(0)
        return minute, randint(0, 59)
    
    def __init__(self):
        self.status = {}
        self.start_minute = 1
        self.total_events = 0

    def ratelimit(self, minute, second):
        print(minute, self.start_minute, self.status, self.total_events)
        if minute != self.start_minute:
            self.start_minute = minute
            self.status.clear()
            self.total_events = 0
        
        if self.total_events > 1000:
            print("not accepting anymore")
            return -1

        hashKey = second % 60
        print("hashkey={}".format(hashKey))
        if hashKey in self.status:
            self.status[hashKey] += 1
        else:
            self.status[hashKey] = 1
        self.total_events += 1

r = RateLimit()
minute = 1    
while 1:
    m,s = r.getTime(minute)
    if r.ratelimit(m, s) == -1:
        minute += 1
        r.getTime(minute)