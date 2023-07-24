from django.shortcuts import render,get_object_or_404,HttpResponse,redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy,reverse
from django.views.generic import *
from django.contrib.auth import get_user_model
from user_data.forms import *
# from blog_app.models import *
User=get_user_model()


# Create your views here.

def SignUp(request):
    if request.method == 'POST':
        user_form=UserCreateForm(request.POST)
        form_profile=profile_form(request.POST, request.FILES)
        if form_profile.is_valid() and user_form.is_valid():
            user=user_form.save()
            form=form_profile.save(commit=False)
            form.user=user
            form.save()
            return redirect(reverse_lazy("user_data:login"))
    return render(request, 'user_data/signup.html',{'Userform':UserCreateForm,'profile_form':profile_form})


class LogIn(TemplateView):
    template_name='user_data/login.html'



# def user_list(request,pk):
#     user=get_object_or_404(User, pk=pk)
#     user_post=posts.objects.filter(user=user)
#     user_profile=profile.objects.filter(user=user)
#     print(user_profile[0].picture)
#     return render(request,'user_data/user.html',{'user_post':user_post,'username':user,'profile':user_profile[0].picture})
