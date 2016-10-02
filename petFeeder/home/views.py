from django.shortcuts import render
from django.views.generic import View
from .code import a
# Create your views here.
class Index(View):
        template_name = 'home/index.html'
       	def get(self, request, *args, **kwargs):
            A = a()
            A.b()
            return render(request, self.template_name,)
