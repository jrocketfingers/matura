from django.shortcuts import render
from models import Question, AnswerType, Answer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def unos(request, number):
    if request.method == 'GET':
        answer_types = AnswerType.objects.all()
        return render(request, 'unos.html', { 'question_number': number, 'answer_types': answer_types })

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
    try:
        page_number = request.GET['page']
    except:
        page_number = 1
    questions_per_page = 5

    start_number = (int(page_number) - 1) * questions_per_page
    questions = Question.objects.all()[start_number : start_number + questions_per_page]
    if len(questions) != 0:
        return render(request, 'prikaz.html', { 'questions': questions})
    else:
        return HttpResponse("Nema toliko pitanja")


def question_number(request, number = 1):
    question = Question.objects.get(number=number)
    questions = [question]

    return render(request, 'prikaz.html', { 'questions': questions })


def overview(request):
    overall_number = 327 # overall number; should get loaded from the settings
    existing_questions = [int(question.number) for question in Question.objects.all()]
    missing_questions = filter(lambda x: x not in existing_questions, range(1, overall_number + 1))
    percentage_complete = len(existing_questions) / (overall_number / 100.0)

    return render(request, 'overview.html', { 'missing_questions': missing_questions, 'percentage_complete': percentage_complete, 'overall_number': overall_number })
