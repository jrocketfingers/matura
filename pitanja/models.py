from django.db import models

class AnswerType(models.Model):
    name = models.CharField(max_length=15)

    def __unicode__(self):
    	return self.name


class Question(models.Model):
    number = models.IntegerField()
    text = models.TextField()
    image = models.ImageField(upload_to='images/')
    answer_type = models.ForeignKey(AnswerType)

    def __unicode__(self):
    	return self.number


class Answer(models.Model):
    text = models.TextField()
    value = models.CharField(max_length=150)
    answer_type = models.ForeignKey(AnswerType)

    def __unicode__(self):
    	return self.text