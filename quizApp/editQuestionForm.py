from django.forms import ModelForm
from .models import quizQuestions
from django import forms

class editQuizForm(ModelForm):
    class Meta:
        model = quizQuestions
        fields = ['id','question', 'option1', 'option2', 'option3', 'option4', 'answer']


