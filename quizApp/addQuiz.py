from django import forms
from .models import quizQuestions, Quiz
from django.forms import inlineformset_factory


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['name', 'author']


class QuestionForm(forms.ModelForm):
    class Meta:
        model = quizQuestions
        fields = ['question', 'option1', 'option2', 'option3', 'option4', 'answer']


QuestionFormSet = forms.inlineformset_factory(Quiz, quizQuestions, form=QuestionForm, extra=1)
