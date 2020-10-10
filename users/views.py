from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.contrib.auth import authenticate

from mains.models import Post
from users.models import MyUser
from .forms import RegisterForm, LoginForm, CreatePost
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as auth_views


def register(request):
    if "usr_id" in request.session:
        user = MyUser.objects.get(id=request.session.get("usr_id")).username
    else:
        user = ""
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # acc  = User(username=form.cleaned_data.get('username'),
            #          email=form.cleaned_data.get('email'),
            #         password=form.cleaned_data.get('password'))
            # acc.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form,
                                                   'user': user})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            if MyUser.objects.filter(username=form.cleaned_data['username'],
                                     password=form.cleaned_data['password']).exists():
                usr = MyUser.objects.get(username=form.cleaned_data['username'],
                                         password=form.cleaned_data['password'])
                request.session['usr_id'] = usr.id
                return redirect('main-home')
            else:
                return redirect('register')



    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


@login_required
def logout_user(request):
    if request.method == "POST":
        del request.session['usr_id']

    return redirect('register')


def profile(request, pk):
    posts = Post.objects.all()
    context = {'posts': posts[::-1]}
    return render(request, 'users/profile.html', context)


def post_details(request, pk):
    post = Post.objects.filter(id=pk).first()
    context = {'post': post}
    return render(request, 'users/post_details.html', context)


def create_post(request):
    if request.method == 'POST':
        form = CreatePost(request.POST)
        if form.is_valid():
            user = MyUser.objects.get(id=request.session.get("usr_id"))
            # acc  = User(username=form.cleaned_data.get('username'),
            #          email=form.cleaned_data.get('email'),
            #         password=form.cleaned_data.get('password'))
            # acc.save()
            pst = Post(title = form.cleaned_data.get('title'), description = form.cleaned_data.get('description'), type = form.cleaned_data.get('type'), author = user, domain = form.cleaned_data.get('domain'))
            pst.save()
            return redirect('main-home')
    else:
        form = CreatePost()
    return render(request, 'users/post_create.html', {'form': form })

def delete_post(request, pk):

    post = Post.objects.get(id = pk)
    post.delete()
    return redirect('main-home')
