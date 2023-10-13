from django.urls import path
from .views import QuestionListView, QuestionUpdateView, QuizFormView, AddQuestionView

urlpatterns = [
    path("", QuizFormView.as_view(), name="home"),
    path("questionEditList", QuestionListView.as_view(), name="questionEditList"),
    path("editQuestion/<int:pk>", QuestionUpdateView.as_view(), name="editQuestion"),
    path("questionAdd", AddQuestionView.as_view(), name="questionAdd"),

]
