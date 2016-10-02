from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from home.models import Date
class Index(View):
        template_name = 'logs/index.html'
       	def get(self, request, *args, **kwargs):
            context = {}
            dates=Date.objects.all()
            print (Date.objects.all())
            context['date_list'] = dates
            return render(request, self.template_name,context)
