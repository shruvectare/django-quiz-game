from django.shortcuts import render
from .models import quizQuestions
from .forms import quizForm

# Create your views here.

def home(request):

    if request.method == 'POST':
        form = quizForm(request.POST)

        if form.is_valid():
            questions = quizQuestions.objects.all()
            score = 0

            context = {}
            for q in questions:

                if q.answer == form.cleaned_data[str(q.id)]:
                    score += 10
                context = {
                    'score': score,
                    'questions': questions,
                    'form' : form
                }
            return render(request, 'home.html', context)
    else:
        questions = quizQuestions.objects.all()
        form = quizForm()
        context = {
            'questions': questions,
            'form': form
        }
        return render(request, 'home.html', context)
