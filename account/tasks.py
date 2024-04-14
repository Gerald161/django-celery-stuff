from celery import shared_task

@shared_task
def add(x, y):
    for i in range(10):
        print(i)
        print("My G what is up")
        
    return x + y

@shared_task
def subs(x):
    print("working")
    return "G"

@shared_task
def my_task():
    for i in range(11):
        print(i)
    return "Task Complete!"