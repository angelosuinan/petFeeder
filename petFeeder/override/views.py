from django.shortcuts import render
from django.utils import timezone
# Create your views here.
from gpiozero import LED
from time import sleep
from home.models import Date
from django.views.generic import View
import time
class Index(View):
        template_name = 'override/index.html'
       	def get(self, request, *args, **kwargs):
            return render(request, self.template_name,)
        def post(self, request, *args, **kwargs):
            q = Date(feed="True", pub_date=timezone.now())
            q.save()
            led= LED(4)
            led.off()
            sleep(2)
           # with open('assets/feed.txt', 'w+') as f:
          #      f.write("0")
            return render(request, 'home/index.html',)
