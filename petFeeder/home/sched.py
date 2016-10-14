from datetime import datetime
from gpiozero import LED
from time import sleep
from .models import Date

from django.utils import timezone

class Sched():

    def start(self):
        with open('assets/sched.txt', 'r') as f:
            if f.readline()=='1':
                return
        with open('assets/sched.txt', 'w+') as f:
            f.write("1")
        print ("SADASDA")
        while True:
            s = str(datetime.time(datetime.now()))
            s=s[0:2]+s[3:5]

            with open('assets/time1.txt', 'r') as f:
                if f.readline()==s:
                    self.feed()
            with open('assets/time2.txt', 'r') as f:
                if f.readline()==s:
                    self.feed()
            with open('assets/time3.txt', 'r') as f:
                if f.readline()==s:
                    self.feed()
    def feed(self,):
        led = LED(4)
        led.off()
        sleep(2)
        q = Date(feed="True", pub_date=timezone.now())
        q.save()
        import pdb
        pdb.set_trace()
