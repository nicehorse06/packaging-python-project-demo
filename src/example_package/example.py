from django.conf import settings

def add_one(number):
    print(dir(settings))
    return number + 1
