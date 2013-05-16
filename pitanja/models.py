from django.db import models

class Question(models.Model):
    number = models.IntegeField()
    text = models.TextField()
    image = models.ImageField()
    answer_type = models.ForeignKey(AnswerType)


class AnswerType(models.Model):
    name = models.CharField(max_length=15)


class Answer(models.Model):
    text = models.TextField()
    value = models.CharField(max_length=150)
    answer_type = models.ForeignKey(AnswerType)
