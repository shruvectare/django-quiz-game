from django.db import models

# Create your models here.

class Quiz(models.Model):
    name = models.TextField(max_length=100, null=True)
    author = models.CharField(max_length=100, null=True)
    dt_date = models.DateTimeField(auto_now_add=True)
    quiz = models.ForeignKey('quizQuestions', on_delete=models.CASCADE, null=True, related_name='related_quiz')

    def __str__(self):
        return self.name


class quizQuestions(models.Model):
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE,null=True, related_name='questions')
    question = models.TextField(max_length=100, null=True)
    option1 = models.CharField(max_length=100, null=True)
    option2 = models.CharField(max_length=100, null=True)
    option3 = models.CharField(max_length=100, null=True)
    option4 = models.CharField(max_length=100, null=True)
    answer = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.question