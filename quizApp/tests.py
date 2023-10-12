from django.test import TestCase
import unittest
from django.test import Client, TestCase

from django.urls import reverse
from .models import quizQuestions
# Create your tests here.
class test_Task (unittest.TestCase):

    def test_check_status_200(self):
         self.client = Client()
         response = self.client.get(reverse('home'))
         # Check if the page loads
         assert response.status_code == 200
         # Check if the quizzes are passed on the template context
         assert "questions" in response.context
         assert "score" not in response.context

    def test_post_cases(self):
        self.client = Client()
        response = self.client.post(reverse('home'), {})


class test_Task1 (TestCase):

    def test_quizzes_displayed_on_page(self):
        # Check if the quizzes are being displayed on the page
        self.client = Client()
        response = self.client.get(reverse('home'))
        questions = quizQuestions.objects.all()
        for quiz in questions:
            self.assertContains(response.body, quiz.question)




