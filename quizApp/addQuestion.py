from django.forms import ModelForm
from .models import quizQuestions
from django import forms

class addQuestion(forms.ModelForm):
    class Meta:
        model = quizQuestions
        fields = ['id','question', 'option1', 'option2', 'option3', 'option4', 'answer']

    def __init__(self, *args, **kwargs):
        self.quiz_id = kwargs.pop('quiz_id', None)  # Pop the quiz_id from kwargs
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(addQuestion, self).save(commit=False)
        if self.quiz_id is not None:
            instance.quiz_id = self.quiz_id  # Set the quiz_id
        if commit:
            instance.save()
        return instance
