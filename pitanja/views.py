from django.shortcuts import render
from models import Question, AnswerType, Answer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def unos(request):    
    if request.method == 'GET':
        answer_types = AnswerType.objects.all()
        return render(request, 'unos.html', { 'answer_types': answer_types })

    elif request.method == 'POST':
        question = Question()
        post_data = request.POST;

        try:
            question.image = request.FILES['image']
        except:
            pass

        question.answer_type = AnswerType.objects.get(name = post_data['type'])
        question.text = post_data['text']
        question.number = post_data['number']

        question.save()

        answers = []
        for key in [x for x in post_data if x.startswith('answer')]:
            current = key.replace('answer', '')

            post_answer = post_data['answer' + current]
            post_solution = post_data['solution' + current]

            if post_answer != '':
                answer = Answer()
                answer.text = post_answer
                answer.value = post_solution
                answer.question = question
                answers.append(answer)

        for answer in answers:
            answer.save()

        answer_types = AnswerType.objects.all()
        return render(request, 'unos.html', \
                     { 'question_number': int(question.number) + 1, \
                       'answer_types': answer_types })

    else:
        return HttpResponse("Method not allowed.", status=405)


def question(request):
    # zasad koristim page parametar za jedno pitanje (id)
    # page = request.GET['page']
    question_number = request.GET['page']
    questions_per_page = 2

    question = Question.objects.get(number=question_number)
    answers = question.answer_set.all()

    return render(request, 'prikaz.html', { 'question': question, 'answers': answers })


def question_number(request, redni_broj=1):
    question = Question.objects.get(number=redni_broj)
    answers = question.answer_set.all()

    return render(request, 'prikaz.html', { 'question': question, 'answers': answers })