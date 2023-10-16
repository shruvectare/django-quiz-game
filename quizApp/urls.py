from django.urls import path
from .views import QuestionListView, QuestionUpdateView, QuizFormView, AddQuestionView, QuizPage

urlpatterns = [
    path("", QuizPage.as_view(), name="mainQuizPage"),
    path("quizList/<int:pk>", QuizFormView.as_view(), name="home"),
    path("questionEditList/<int:pk>", QuestionListView.as_view(), name="questionEditList"),
    path("editQuestion/<int:pk>", QuestionUpdateView.as_view(), name="editQuestion"),
    path("questionAdd/<int:pk>", AddQuestionView.as_view(), name="questionAdd"),

]
