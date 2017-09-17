from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("Hello World. You're at the polls index")

def detail(request, question_id):
	return HttpResponse("You're looking at question {0}".format(question_id))

def results(request, question_id):
	response = "You're looking at the results of question {0}".format(question_id)
	return HttpResponse(response)

def vote(request, question_id):
	return HttpResponse("You're voting on question {0}".format(question_id))
