from django import forms
from .models import quizQuestions

class quizForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        quiz_questions = quizQuestions.objects.all()
        for q in quiz_questions:
            options = [
                (q.option1, q.option1),
                (q.option2, q.option2),
                (q.option3, q.option3),
                (q.option4, q.option4)
            ]
            self.fields[str(q.id)] = forms.CharField(label = q.question, widget=forms.RadioSelect(choices=options))