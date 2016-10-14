from django.shortcuts import render
from django.views.generic import View
from .code import a
import threading
from .cat import Cam
from django.utils import timezone
from .models import Date
import re
# Create your views here.
c= Cam()
class Index(View):
        template_name = 'home/index.html'
        def get(self, request, *args, **kwargs):
            t =threading.Thread(target=c.start)
            if Date:
                d = Date.objects.latest('pub_date')
                date = d.pub_date
                match = re.search('(([0-9])\w+)', date)
                if match:
                    date = match.group()
                    print (date)
            return render(request, self.template_name,)
        def post(self, request, *args, **kwargs):

            time1 = request.POST.get('time1')
            print (time1)
            if time1:
                with open ("assets/time1.txt", 'w+') as f:
                    f.write(time1)
            time2 = request.POST.get('time2')
            if time2:
                with open ("assets/time2.txt", 'w+') as f:
                    f.write(time2)
            time3 = request.POST.get('time3')
            if time3:
                with open ("assets/time3.txt", 'w+') as f:
                    f.write(time3)
            if not time1 and not time2 and not time3:
                if 'feed' in request.POST:
                    A = a()
                    A.rage_feed()
            print ("ASAS")
            return render(request, self.template_name,)
