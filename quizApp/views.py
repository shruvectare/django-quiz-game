from django.shortcuts import render, redirect
from django.urls import reverse

from .models import quizQuestions
from .forms import quizForm
from .editQuestionForm import editQuizForm

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

def questionEditList(request):
    questions = quizQuestions.objects.all()
    context = {
        'questions': questions,
    }
    return render(request, 'questionEditList.html', context)

def editQuestion(request):
    qid = request.POST["questID"]
    question = quizQuestions.objects.get(id=qid)
    if request.method == "POST" :
        editform = editQuizForm(request.POST, instance=question)
        if editform.is_valid():
            editform.save()

            return redirect(reverse('home'))

        else :
            form = editQuizForm(instance=question)
            context = {
                'id' : qid,
                'question' : question,
                'form' :  form
            }
            return render(request, 'questionEdit.html', context)

