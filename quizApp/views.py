from django.shortcuts import render
from .models import quizQuestions


# Create your views here.

def home(request):
    if request.method == 'POST':
        print(request.POST)
        questions = quizQuestions.objects.all()
        score = 0
        context = {}
        for q in questions:
            print(request.POST.get(q.question))
            print(q.answer)
            print()
            if q.answer == request.POST.get(q.question):
                score += 10
            context = {
                'score': score,
                'questions': questions
            }
        return render(request, 'home.html', context)
    else:
        questions = quizQuestions.objects.all()
        return render(request, 'home.html', {'questions': questions})
