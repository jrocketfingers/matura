from django.shortcuts import render
from models import Question, AnswerType, Answer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

def unos(request):
    answer_types = AnswerType.objects.all()
    return render(request, 'unos.html', { 'answer_types': answer_types })

@csrf_exempt
def question(request):
    if request.method == 'GET':
        pass

    elif request.method == 'POST':
        question = Question()
        post_data = request.POST;

        try:
            question.image = request.FILES['image']
        except:
            print 'exception'

        question.answer_type = AnswerType.objects.get(name = post_data['type'])
        question.text = post_data['text']
        question.number = post_data['number']

        answers = []

        for key in [x for x in post_data if x.startswith('answer')]:
            current = key.replace('answer', '')

            post_answer = post_data['answer' + current]
            post_solution = post_data['solution' + current]

            answer = Answer()
            answer.text = post_answer
            answer.value = post_solution
            answer.question = question
            answers.append(answer)

        question.save()
        (answer.save() for answer in answers)

        return HttpResponse("Question created.", status=201)

    else:
        return HttpResponse("Method not allowed.", status=405)