from django.db import models

class AnswerType(models.Model):
    name = models.CharField(max_length=15)

    def __unicode__(self):
        return self.name


class Question(models.Model):
    number = models.IntegerField(unique=True)
    text = models.TextField(blank=False)
    image = models.ImageField(upload_to='images/', null=True)
    answer_type = models.ForeignKey(AnswerType)

    def __unicode__(self):
        return str(self.number)


class Answer(models.Model):
    text = models.TextField(blank=False)
    value = models.CharField(max_length=150, blank=False)
    question = models.ForeignKey(Question)

    def __unicode__(self):
        return self.text

    def format_dopunjavanje(self):
        replace_html = "<input name='answer' class='input span2' data-solution='{}' type='text'></input>"
        solutions = self.value.split(';')
        return self.text.replace('%', replace_html).format(*solutions)