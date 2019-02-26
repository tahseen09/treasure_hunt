from django.shortcuts import render, HttpResponse
from . models import clues, users
from . forms import Form, submit_form
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

#code flow: check if there is any form post method -> if ans found in db, generate next question -> else load same question 

def index(request):
    msg = None
    next_ques = None
    if request.method == "POST":
        form = Form(request.POST)
        ans = request.POST.get("ans")
        print(ans)
        ques_id = request.POST.get("id")
        print(ques_id)
        check = clues.objects.filter(ans=ans, ques_id=ques_id).exists()
        if check:
            try:
                next_ques = clues.objects.get(prev_ans=ans, ques_id=int(ques_id)+1)
            except ObjectDoesNotExist:
                return render(request, 'final.html')
            #if int(next_ques.ques_id)+1 > 3:
                #return render(request, 'final.html')
            #else:
            return render(request, 'index.html', {'next':next_ques})
        else:
            #if answer is wrong
            msg = "Sorry! Try again"
            next = clues.objects.get(ques_id=ques_id)
            return render(request,'index.html',{'msg':msg, 'next':next})

    else:
        i=1
        next_ques = clues.objects.get(ques_id=i)
        return render(request, 'index.html', {'next':next_ques})

def final(request):
    if request.method == "POST":
        form = submit_form(request.POST)
        team_name=request.POST.get("name")
        team_id=request.POST.get("id")
        u = users(name=team_name, team_id= team_id)
        u.save()
        return HttpResponse("Thank you for participating.")