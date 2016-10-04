from gpiozero import LED
from time import sleep
from django.utils import timezone
from .models import Date
class a():

    def b(self):
      #  q = Date(feed="True", pub_date=timezone.now())
       # q.save() # to edit last elememt of a database
        if Date.objects.all():
            d = Date.objects.latest('pub_date')
            led = LED(4)
            led.off()
            sleep(2)
            print (d.feed,"dasda")
            with open ("assets/feed.txt", 'w+') as f:
                f.write("0")
    def rage_feed(self):
        print ("assas")
        q = Date(feed="True", pub_date=timezone.now())
        q.save()
