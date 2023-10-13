from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, ListView, UpdateView, CreateView

from .models import quizQuestions
from .forms import quizForm
from .editQuestionForm import editQuizForm
from django.views import View
from .addQuestion import addQuestion

# Create your views here.

# def home(request):
#     if request.method == 'POST':
#         form = quizForm(request.POST)
#         if form.is_valid():
#             questions = quizQuestions.objects.all()
#             score = 0
#             context = {}
#             for q in questions:
#
#                 if q.answer == form.cleaned_data[str(q.id)]:
#                     score += 10
#                 context = {
#                     'score': score,
#                     'questions': questions,
#                     'form' : form
#                 }
#             return render(request, 'home.html', context)
#     else:
#         questions = quizQuestions.objects.all()
#         form = quizForm()
#         context = {
#             'questions': questions,
#             'form': form
#         }
#         return render(request, 'home.html', context)

class QuizFormView(FormView):
    template_name = 'home.html'
    form_class = quizForm

    def form_valid(self, form):
        questions = quizQuestions.objects.all()
        score = 0
        context = {}
        for q in questions:

            if q.answer == form.cleaned_data[str(q.id)]:
                score += 10
            context = self.get_context_data()
            context["score"] = score
        return render(self.request, self.template_name, context)


class QuestionListView(ListView):
    template_name = 'questionEditList.html'
    model = quizQuestions


class QuestionUpdateView(UpdateView):
    template_name = 'questionEdit.html'
    model = quizQuestions
    form_class = editQuizForm
    success_url = reverse_lazy('home')


class AddQuestionView(CreateView):
    template_name = "addQuestion.html"
    form_class = addQuestion
    success_url = reverse_lazy('home')


