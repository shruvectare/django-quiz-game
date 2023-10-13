from django.forms import ModelForm
from .models import quizQuestions
from django import forms

class addQuestion(forms.ModelForm):
    class Meta:
        model = quizQuestions
        fields = '__all__'


