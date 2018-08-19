from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.http import Http404
from django.urls import reverse

# Create your views here.
def index(request):
	return HttpResponse("Hello world. You're at the polls index.")

# def detail(request, question_id):
# 	return HttpResponse("You're looking at question %s."%question_id)

def results(request, question_id):
	# response = "You're looking at the results of question %s ."
	# return HttpResponse(response % question_id)
	question = get_object_or_404(Question, pk=question_id)
	return render(request , 'polls/results.html' , {'question': question})

def vote(request, question_id):
	# return HttpResponse("You're voting on question %s ." % question_id)
	question = get_object_or_404(Question, pk = question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError , Choice.DoesNotExist):
		return render(request , 'polls/detail.html', { 'question': question ,
			'error_message': "You didn't select a choice ." ,})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# def index(request):
# 	latest_question_list = Question.objects.order_by('-pub_date')[:5]
# 	output = ', '.join([q.question_text for q in latest_question_list])
# 	return HttpResponse(output)
# def index(request):
# 	latest_question_list = Question.objects.order_by('-pub_date')[:5]
# 	template = loader.get_template('polls/index.html')
# 	context = {
# 		'latest_question_list' : latest_question_list,
# 	}
# 	return HttpResponse(template.render(context, request))
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {
		'latest_question_list' : latest_question_list,
	}
	return render(request, 'polls/index.html', context)
#Note that in last index() , we donot need to import loader and HttpResponse .


#Using get() and Http404() in detail() for error handling .
# def detail(request, question_id):
# 	try:
# 		question = Question.objects.get(pk=question_id)
# 	except Exception as e:
# 		raise Http404("Question does not exist !! ")
# 	return render(request, 'polls/detail.html', {'question': question})

#Shortcut for detail() using get_object_or_404()
def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html' , {'question': question})
