from django.test import TestCase

from hello_world.models import *


class SearchTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        _unit = Unit.objects.create(name="testView")

        for i in range(15):
            _thread = Thread.objects.create(
                name=f"test{i}", text=f"test{i}_text", unit=_unit
            )
            for j in range(15):
                Comment.objects.create(text=f"test{j}", thread=_thread)

    def test_checkView(self):
        response = self.client.get('/utils/search?pattern=test')
        self.assertEqual(response.status_code, 200)
