from django.http.response import HttpResponse
from .tasks import add, subs
from django_celery_beat.models import PeriodicTask, IntervalSchedule, CrontabSchedule
import json

#cache stuff below
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.response import Response
from rest_framework.views import APIView
import time
import random


class ProfileView(APIView):
    # With auth: cache requested url for each user for 2 hours
    # @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(cache_page(10))
    def get(self, request):
        time.sleep(5)

        random_number = random.randint(0, 10)

        content = {
            "user_feed": "really long feed",
            "num": random_number
        }
        return Response(content)
    

class ProfileView2(APIView):
    # With auth: cache requested url for each user for 2 hours
    # @method_decorator(cache_page(60 * 60 * 2))
    def get(self, request):
        time.sleep(5)

        random_number = random.randint(0, 10)

        content = {
            "user_feed": "really long feed",
            "num": random_number
        }
        return Response(content)

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