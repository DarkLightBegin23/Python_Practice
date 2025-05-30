# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question

def index(request):
    question_list = Question.objects.order_by("-create_date")
    context = {'question_list' : question_list}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get("content"), create_date=timezone.now())
    # 임의 변수 넣어서 save() 메서드 써도 됨
    return redirect('pybo:detail', question_id=question.id)