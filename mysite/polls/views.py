from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from polls.forms import QuestionForm
from polls.models import Question, Choice


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def display_data(request):
    context = {
        "a": [1,2,4,5],
        "b": ["a", "b", "c", "d"],
        "c": {"fname": "F name", "lname": "L name"}
    }
    return render(request, "display_data.html", {"data": context})


def create_question(request):
    if request.method == "GET":
        return render(request, "polls/create.html", {})
    
    if request.method == "POST":
        # Reading the question data
        question_text = request.POST.get("question_text")
        pub_date = request.POST.get("pub_date")
        
        # Here I am creating the Question
        question = Question.objects.create(question_text=question_text, pub_date=pub_date)
        
        # Reading the Choice -1 data and creating Choice
        question.choice_set.create(
            choice_text=request.POST.get("choice_text1"),
            votes=request.POST.get("votes1")
        )

        question.choice_set.create(
            choice_text=request.POST.get("choice_text2"),
            votes=request.POST.get("votes2")
        )

        question.choice_set.create(
            choice_text=request.POST.get("choice_text3"),
            votes=request.POST.get("votes3")
        )
        return HttpResponseRedirect(reverse('polls:detail', args=(question.id,)))
    

def create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            # Need to do some operation
            form.save()
        else:
            # Need to show the error to the user
            return render(request, "polls/create_form.html", {"form": form})
    else:
        form = QuestionForm()
    return render(request, "polls/create_form.html", {"form": form})
