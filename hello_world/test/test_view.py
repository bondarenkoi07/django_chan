from django.test import TestCase

from hello_world.models import Unit, Thread


class TestView(TestCase):
    @classmethod
    def setUpTestData(cls):
        for i in range(10):
            _unit = Unit.objects.create(name=f'test{i}')
            for j in range(10):
                Thread.objects.create(name=f'Thread{j}', text=f'Test{j}', unit=_unit)

    def test_access_thread(self):

        pass
