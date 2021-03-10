import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning.settings")

import django

django.setup()

from hello_world.models import *

thread = Thread.objects.all().delete()

folder = 'media'
for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        #elif os.path.isdir(file_path): shutil.rmtree(file_path)
    except Exception as e:
        print(e)