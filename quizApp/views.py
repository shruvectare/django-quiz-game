from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, ListView, UpdateView, CreateView

from .models import quizQuestions, Quiz
from .forms import quizForm
from .editQuestionForm import editQuizForm
from django.views import View
from .addQuestion import addQuestion

# Create your views here.

class QuizFormView(FormView):
    template_name = 'home.html'
    form_class = quizForm
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['quiz_id'] = self.kwargs['pk']
        return kwargs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quiz_id'] = self.kwargs['pk']
        return context
    def form_valid(self, form):
        quiz_id = self.kwargs['pk']
        print(quiz_id)
        questions = quizQuestions.objects.filter(quiz_id=quiz_id)
        score = 0
        context = {}
        for q in questions:

            if q.answer == form.cleaned_data[str(q.id)]:
                score += 10
            context = self.get_context_data()
            context["score"] = score
            context["quiz_id"] = quiz_id
        return render(self.request, self.template_name, context)


class QuestionListView(ListView):
    template_name = 'questionEditList.html'
    model = quizQuestions

    def get_queryset(self):
        quiz_id = self.kwargs.get('pk')
        queryset = super().get_queryset().filter(quiz_id = quiz_id)
        return queryset


class QuestionUpdateView(UpdateView):
    template_name = 'questionEdit.html'
    model = quizQuestions
    form_class = editQuizForm
    success_url = reverse_lazy('mainQuizPage')


class AddQuestionView(CreateView):
    template_name = "addQuestion.html"
    form_class = addQuestion
    success_url = reverse_lazy('mainQuizPage')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['quiz_id'] = self.kwargs['pk']
        return kwargs

class QuizPage(ListView):
    template_name = 'mainQuizPage.html'
    model = Quiz

