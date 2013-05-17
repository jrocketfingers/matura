from django.shortcuts import render
from models import Question, AnswerType, Answer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

def unos(request):
    return render(request, 'unos.html')

@csrf_exempt
def upload(request):
	pera = Question()
	pera.answer_type = AnswerType.objects.get(id=1)
	pera.text = "Proba"
	pera.number = 5
	print request.FILES['slika']
	pera.image = request.FILES['slika']
	pera.save()
	return HttpResponse(request.POST)