from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, ListView, UpdateView, CreateView
from .models import quizQuestions, Quiz
from .forms import quizForm
from .editQuestionForm import editQuizForm
from django.views import View
from .addQuestion import addQuestion
from django.forms import inlineformset_factory, modelformset_factory
from .addQuiz import QuizForm, QuestionForm, QuestionFormSet


# Create your views here.

class QuizFormView(FormView):
    template_name = 'home.html'
    form_class = quizForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['quiz_id'] = str(self.kwargs['pk'])
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
        queryset = super().get_queryset().filter(quiz_id=quiz_id)
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


def AddQuizView(request):
    QuestionFormSet = modelformset_factory(quizQuestions, fields=('question', 'option1', 'option2', 'option3', 'option4', 'answer'))
    if request.method == 'POST':
        quiz_form = QuizForm(request.POST)
        question_formset = QuestionFormSet(request.POST)
        print("-----------")
        if question_formset.is_valid() :
            new_quiz = quiz_form.save()

            return redirect('AddQuizView')


        if quiz_form.is_valid() and question_formset.is_valid():
            print("-----------")
            new_quiz = quiz_form.save(commit=False)
            questions = question_formset.save(commit=False)
            for q in questions:
                q.quiz = new_quiz
                q.save()
            return redirect('addQuizView')

    else:
        quiz_form = QuizForm()
        question_formset = QuestionFormSet(queryset=quizQuestions.objects.none())

    return render(request, 'addQuiz.html', {'quiz_form': quiz_form, 'question_formset': question_formset})


class AddQuiz(CreateView):
    template_name = 'addQuiz.html'
    form_class = QuizForm
    model=Quiz
    success_url = reverse_lazy('mainQuizPage')
    def __init__(self):
        super().__init__()
        self.question_formset = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            self.question_formset = QuestionFormSet(self.request.POST)
        else :
            self.question_formset = QuestionFormSet()
        context['question_formset'] = self.question_formset
        return context

    def form_valid(self, form):

        context = self.get_context_data()
        question_formset = context['question_formset']
        quiz = form.save()
        if question_formset.is_valid():
            question_formset.instance = quiz
            question_formset.save()
        return super().form_valid(form)
