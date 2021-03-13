import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning.settings")

import django

django.setup()

from hello_world.models import *

try:
    thread = Thread.objects.all().delete()
except:
    print("We are not prepared for makemigrations")
