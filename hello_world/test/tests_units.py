import random
import string

from django.db import models
from django.test import TestCase

# Create your tests here.
from hello_world.models import Unit, Thread


class QueueThreadTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        _unit = Unit.objects.create(name='test')
        rand_str = lambda n: ''.join([random.choice(string.ascii_lowercase) for _ in range(n)])

        for i in range(10):
            Thread.objects.create(name=f'Thread{i}', text=f'Test{i}', unit=_unit)
        Thread.objects.create(name=f'Thread11', text=rand_str(1025), unit=_unit)

    def test_last_thread(self):
        max_prior = Thread.objects.filter(unit=Unit.objects.get(name='test')).aggregate(models.Max('priority'))[
            'priority__max']
        self.assertEqual(max_prior, 11, msg="a&")

    def test_text_name(self):
        _thread = Thread.objects.get(id=11)
        max_length = _thread._meta.get_field('text').max_length
        self.assertEqual(max_length, 1024)





