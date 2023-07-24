from django.shortcuts import render,get_object_or_404,HttpResponse,redirect
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from home_page.models import *
from home_page.forms import *
User = get_user_model()
# Create your views here.

@login_required
def home_page_view(request):

    tasks_to_me=taskModel.objects.filter(assigned_to=request.user).order_by('-id')[:3]
    message_to_me= messageModel.objects.filter(to_user=request.user).order_by('-id')[:3]
    return render(request, 'home_page/home_page.html',{'user':User,'messages':message_to_me,'tasks':tasks_to_me})

@login_required
def TasksView(request):

    tasks_to_me=taskModel.objects.filter(assigned_to=request.user)
    tasks_by_me=taskModel.objects.filter(assigned_by=request.user).order_by('-id')
    tasks_not_completed=tasks_to_me.filter(mark_as_done=False).order_by('-id')
    tasks_completed=taskModel.objects.filter(mark_as_done=True).order_by('-id')
    return render(request, 'home_page/tasks.html',{'metask':tasks_not_completed,'bytask':tasks_by_me,'completed':tasks_completed})

@login_required
def taskDetail(request,pk):

    task=taskModel.objects.filter(pk=pk)[0]

    if request.method == 'POST':

        task.marked()

    return render(request,'home_page/taskmodel_detail.html',{'task':task})

@login_required
def NewTask(request):
    if request.method == 'POST':
        form=taskForm(request.POST)
        if form.is_valid():
            new=form.save(commit=False)
            new.assigned_by=request.user
            new.save()
            return redirect("home_page:tasks")
    return render(request, 'home_page/task_form.html',{'task':taskForm})


class TaskDelete(DeleteView,LoginRequiredMixin):
    login_url='user_data:login'
    model=taskModel
    success_url=reverse_lazy("home_page:tasks")

@login_required
def MessageView(request):

    message_to_me= messageModel.objects.filter(to_user=request.user).order_by('id')

    non_duplicate_set=set()
    messege_dictionary={}

    for message in message_to_me:
        non_duplicate_set.add(message.from_user)

    for user in non_duplicate_set:
        set_query=message_to_me.filter(from_user=user)
        messege_dictionary[user]=set_query
    return render(request,'home_page/messages.html',{'messages':messege_dictionary})

@login_required
def message_detail_view(request,pk):

    to=get_object_or_404(User, pk=pk)

    messages_by=messageModel.objects.filter(from_user = pk)
    messagesby = messages_by.filter(to_user = request.user.pk).order_by('-time_sent')

    messages_to=messageModel.objects.filter(to_user = pk)
    messagesto=messages_to.filter(from_user = request.user).order_by('-time_sent')


    if request.method =='POST':

        message=messageForm(request.POST)

        if message.is_valid():

            msg=message.save(commit=False)
            msg.to_user=to
            msg.from_user=request.user
            msg.save()
            return render(request,'home_page/message_detail.html',{'messages':messagesby,'msg':messagesto,'form':messageForm})
        

    return render(request,'home_page/message_detail.html',{'messages':messagesby,'msg':messagesto,'form':messageForm})



def CreateMessage(request):
    if request.method == 'POST':
        form=newmessageForm(request.POST)
        if form.is_valid():
            new=form.save(commit=False)
            new.from_user=request.user
            new.save()
            return redirect("home_page:messages")
    return render(request,'home_page/message_form.html',{'form':newmessageForm})
