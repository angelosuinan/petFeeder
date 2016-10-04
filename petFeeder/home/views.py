from django.shortcuts import render
from django.views.generic import View
from .code import a
import threading
from .cat import Cam
# Create your views here.
c= Cam()
class Index(View):
        template_name = 'home/index.html'
        def get(self, request, *args, **kwargs):
            t =threading.Thread(target=c.start)
            t.start()
            return render(request, self.template_name,)
        def post(self, request, *args, **kwargs):
            A = a()
            A.b()
            return render(request, self.template_name,)
