from django.http.response import HttpResponse
from .tasks import add, subs
from django_celery_beat.models import PeriodicTask, IntervalSchedule, CrontabSchedule
import json

# Create your views here.
def test(request):
    add.delay(1,2)
    subs.delay(1)
    return HttpResponse("Done")

def dynamicSchedule(request):
   interval, _ = IntervalSchedule.objects.get_or_create(
        every=30,
        period= IntervalSchedule.SECONDS,
    )
    
   PeriodicTask.objects.create(
        interval=interval,
        name="my-schedule",
        task="account.tasks.my_task",
        #args=json.dumps(["Arg1", "Arg2"])
        #one_off=True
    )
   
   return HttpResponse("Donneee")

def secondDynamicSchedule(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour=14, minute=48)
    task = PeriodicTask.objects.create(crontab=schedule, name="unique_name55", task='account.tasks.add', args=json.dumps([1,2]))
    return HttpResponse("Donneee")