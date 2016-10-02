
from django.utils import timezone
from .models import Date
class a():

    def b(self):
        q = Date(feed="True", pub_date=timezone.now())
        q.save()
        print (q,"dasda")
