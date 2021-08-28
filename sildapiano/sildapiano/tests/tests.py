from django.test import TestCase, Client
from django.urls import reverse
from sildapiano.sildapiano import public
from .models import *
import json


class TestViews(TestCase):

    def test_catalogue_GET(self):
        client = Client()

        response = client.get(reverse('catalogue'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "./catalogue.html")

