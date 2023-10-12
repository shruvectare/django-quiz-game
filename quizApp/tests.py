from django.test import TestCase
import unittest
from django.test import Client, TestCase

from django.urls import reverse
from .models import quizQuestions
from .forms import quizForm
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

    # def test_post_cases(self):
    #     self.client = Client()
    #     response = self.client.post(reverse('home'), {})

    def test_quizzes_displayed_on_page(self):
        # Check if the quizzes are being displayed on the page
        self.client = Client()
        response = self.client.get(reverse('home'))
        questions = quizQuestions.objects.all()
        for quiz in questions:
            assert quiz.question in str(response.content.decode("utf-8"))

    def test_submit_all_correct_answers(self):
        # Simulate a POST request with correct answers
        questions = quizQuestions.objects.all()
        self.client = Client()
        response = self.client.post(reverse('home'), {
            "Which one is not a Hogwarts house?": "Dragonheart",
            "What spell did Harry use to kill Lord Voldemort?": "Expelliarmus",
            "Where does Hermione brew her first batch of Polyjuice Potion?": "Moaning Myrtle’s Bathroom",
            "From what King’s Cross platform does the Hogwarts Express leave?": "Nine and Three-quarters",
            "What position does Harry play on the Gryffindor Quidditch team?": "Seeker"
        })

        assert response.status_code == 200  # Check the page redirects you (HTTP 302
        assert "score" in response.context
        s = response.context['score']
        self.assertEqual(s, 50)
    #
    def test_submit_some_correct_answers(self):
        # Simulate a POST request with correct answers
        questions = quizQuestions.objects.all()
        self.client = Client()
        response = self.client.post(reverse('home'), {
            "Which one is not a Hogwarts house?": "Ravenclaw",
            "What spell did Harry use to kill Lord Voldemort?": "Expelliarmus",
            "Where does Hermione brew her first batch of Polyjuice Potion?": "Moaning Myrtle’s Bathroom",
            "From what King’s Cross platform does the Hogwarts Express leave?": "Nine and Three-quarters",
            "What position does Harry play on the Gryffindor Quidditch team?": "Keeper"
        })

        assert response.status_code == 200  # Check the page redirects you (HTTP 302
        assert "score" in response.context
        s = response.context['score']
        self.assertEqual(s, 30)









