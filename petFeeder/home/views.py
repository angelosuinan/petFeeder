from django.shortcuts import render
from django.views.generic import View
from .code import a
import threading
from .cat import Cam
from django.utils import timezone
from .models import Date
import re
from .sched import Sched
# Create your views here.
c= Sched()
class Index(View):
        template_name = 'home/index.html'
        def get(self, request, *args, **kwargs):
            context = self.get_context()
            t =threading.Thread(target=c.start)
            t.start()
            return render(request, self.template_name,context)
        def post(self, request, *args, **kwargs):
            context = self.get_context()
            time1 = request.POST.get('time1')
            print (time1)
            if time1:
                time1 = time1[0:2]+time1[3:5]
                with open ("assets/time1.txt", 'w+') as f:
                    f.write(time1)
            time2 = request.POST.get('time2')
            if time2:
                time2 = time2[0:2]+time2[3:5]
                with open ("assets/time2.txt", 'w+') as f:
                    f.write(time2)
            time3 = request.POST.get('time3')
            if time3:
                time3 = time3[0:2]+time3[3:5]
                with open ("assets/time3.txt", 'w+') as f:
                    f.write(time3)
            if not time1 and not time2 and not time3:
                if 'feed' in request.POST:
                    A = a()
                    A.rage_feed()
            print ("ASAS")
            return render(request, self.template_name,context)
        def get_context(self,):
            context = {}
            time1=""
            time2=""
            time3=""
            with open('assets/time1.txt', 'r') as f:
                time1 =f.readline()
                time1 = time1[0:2]+":"+time1[2:4]
            with open('assets/time2.txt', 'r') as f:
                time2 = f.readline()
                time2 = time2[0:2]+":"+time2[2:4]
            with open('assets/time3.txt', 'r') as f:
                time3 = f.readline()
                time3 = time3[0:2]+":"+time3[2:4]
            time_list=[time1,time2,time3]
            context["time_list"]=time_list
            return context
