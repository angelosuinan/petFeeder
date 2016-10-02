from django.shortcuts import render

# Create your views here.
import home.models
from django.views.generic import View
class Index(View):
        template_name = 'override/index.html'
       	def get(self, request, *args, **kwargs):
            return render(request, self.template_name,)
