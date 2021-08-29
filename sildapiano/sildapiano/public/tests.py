# from django.test import TestCase, Client
# from django.urls import reverse
# from .models import LessonPlans
#
#
# # Create your tests here.
# class TestViews(TestCase):
#
#     def test_lessons_info_GET(self):
#         client = Client()
#         response = client.get(reverse('list'))
#
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, './catalogue.html')

#######################################################################
# import unittest
# from django.test import TestCase
# from .models import LessonPlans
#
#
# class LessonTestCase(TestCase):
#     def setUp(self):
#         LessonPlans.objects.create(lesson_name="Test1", number_of_lessons="1")
#         LessonPlans.objects.create(lesson_name="Test2", number_of_lessons="2")
#
#     def test_lesson_plan(self):
#         """"""
#         test1 = LessonPlans.objects.get(lesson_name="Test1")
#         test2 = LessonPlans.objects.get(lesson_name="Test2")
#
#         self.assertEqual(test1.lesson_name(), "Test1")
#         self.assertEqual(test2.lesson_name(), "Test2")
#
#
# if __name__ == '__main__':
#     unittest.main()

##################################################################

# from django.test import TestCase
# from django.urls import reverse
#
# from .models import *
#
#
# class LessonTestCase(TestCase):
#
#     def setUp(self):
#         LessonPlans.objects.create(lesson_name="Test1", description="TEST1 decription",
#                                    number_of_lessons="1", price_for_all=10)
#         LessonPlans.objects.create(lesson_name="Test2", description="TEST2 decription",
#                                    number_of_lessons="2", price_for_all=20)
#
#     def test_view_url_exists_at_desired_location(self):
#         response = self.client.get('./catalogue.html')
#         self.assertEqual(response.status_code, 200)
#
#     def test_view_uses_correct_template(self):
#         response = self.client.get(reverse('authors'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, './catalogue.html')
##################################################################
#
# from django.test import TestCase
#
# from .models import LessonPlans
#
#
# class TestViews(TestCase):
#
#     def setUp(self):
#         LessonPlans.objects.create(lesson_name="Test1", description="TEST1 decription",
#                                    number_of_lessons=1, price_for_all=10)
#         LessonPlans.objects.create(lesson_name="Test2", description="TEST2 decription",
#                                    number_of_lessons=2, price_for_all=20)
#
#     def test_lesson_plan(self):
#         """"""
#         test1 = LessonPlans.objects.get(lesson_name="Test1")
#         test2 = LessonPlans.objects.get(lesson_name="Test2")
#
#         self.assertEqual(test1.lesson_name(), "Test1")
#         self.assertEqual(test2.lesson_name(), "Test2")


###################################################################

from django.test import TestCase
from django.urls.base import resolve
from .views import contacts


class TestsUrls(TestCase):

    def test_contacts(self):
        found = resolve('/contacts')
        self.assertEqual(found.func, contacts)
