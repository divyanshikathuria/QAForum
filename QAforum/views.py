from django.shortcuts import render
import datetime
from models import *
from django.db.models import Max
from django.contrib.auth.models import User
from django.http import HttpResponse


def register(request):
    return render(request,'reg.html')

def login(request):
    return render(request,'login.html')
    
def home(request):
    
    question = Question.objects.aggregate(Max('id'))
    a = question['id__max']
    questlist = []
    for i in range(a):
        q = Question.objects.get(id=(a-i))
        questlist.append(q)
    return render(request,'home.html',{'l':questlist, 'an':a})

def display(request):
    return render(request,'post.html')
    
def question(request):
    if 'postt' in request.GET:
        quest = request.GET['quest']
        
        user_id= request.user.id
        user = User.objects.get(id = user_id)
        date_created = datetime.datetime.now()
        date_updated = datetime.datetime.now()
        obj = Question(title=quest,user_id=user,date_created=date_created,date_update=date_updated)
        obj.save()
        return HttpResponse("success")
        
        
def writeans(request,ques_id):
    quest=Question.objects.get(id=ques_id)
    
    anss = Answer.objects.filter(question_id_id=ques_id).aggregate(Max('id'))
    a = anss['id__max']
    answerlist = []
    if(a>1):
        for i in range(a):
            q = Answer.objects.get(id=(a-i))
       	    answerlist.append(q)
    return render(request,'ans.html',{'q':quest,'a':answerlist})
    
def answer(request,ques_id):
    if 'ans' in request.GET:
        answer = request.GET['answer']
        ques_obj=Question.objects.get(id=ques_id)
        user_id= request.user.id
      
        user = User.objects.get(id = user_id)
        obj = Answer(answer_text=answer,user_id=user,question_id_id=ques_id)
        obj.save()
        
    
        anss = Answer.objects.filter(question_id_id=ques_id).aggregate(Max('id'))
        a = anss['id__max']
        answerlist = []
        if(a>1):
            for i in range(a):
                q = Answer.objects.get(id=(a-i))
       	        answerlist.append(q)
        return render(request,'after.html',{'a':answerlist})
        
        
        
        
           


