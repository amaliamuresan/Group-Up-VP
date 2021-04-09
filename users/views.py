import os

from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from mains.models import Post, PostDomain, PostType
from users.models import MyUser
from .forms import RegisterForm, LoginForm, CreatePost, UpdatePost



def register(request):
    if "usr_id" in request.session:
        user = MyUser.objects.get(id=request.session.get("usr_id")).username
    else:
        user = ""
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            if MyUser.objects.filter(username=form.cleaned_data['username']).exists():
                messages.error(request, "Username already exists!")
                return redirect('main-home')
            else:
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



def logout_user(request):
    if request.method == "POST":
        del request.session['usr_id']

    return redirect('register')


def profile(request, pk):
    user = MyUser.objects.filter(id=pk).first()
    posts = Post.objects.all()
    context = {'posts': posts[::-1], 'user': user}
    return render(request, 'users/profile.html', context)


def post_details(request, pk):
    post = Post.objects.filter(id=pk).first()
    context = {'post': post}
    return render(request, 'users/post_details.html', context)


def create_post(request):
    '''
    if request.method == 'POST':
        form = CreatePost(request.POST)
        if form.is_valid():
            user = MyUser.objects.get(id=request.session.get("usr_id"))
            # acc  = User(username=form.cleaned_data.get('username'),
            #          email=form.cleaned_data.get('email'),
            #         password=form.cleaned_data.get('password'))
            # acc.save()
            pst = Post(title=form.cleaned_data.get('title'), description=form.cleaned_data.get('description'),
                       type=form.cleaned_data.get('type'), author=user, domain=form.cleaned_data.get('domain'))
            pst.save()
            return redirect('main-home')
    else:
        form = CreatePost()
    return render(request, 'users/post_create.html', {'form': form})
    '''

    domains = PostDomain.objects.all()
    types = PostType.objects.all()

    if request.method == 'POST':
        user = MyUser.objects.get(id=request.session.get("usr_id"))
        title = request.POST.get('title')
        type = request.POST.get('type')
        domain = request.POST.get('domain')
        description = request.POST.get('description')
        post = Post(title=title, description=description, type=type, author=user, domain=domain)
        post.save()
        messages.success(request, "Post " + post.title + " created!")
        return redirect('main-home')
    return render(request, 'users/post_create.html', {'types':types, 'domains':domains})

def delete_post(request, pk):
    user = MyUser.objects.get(id=request.session.get("usr_id"))
    post = Post.objects.get(id=pk)
    post_title = post.title
    post.delete()
    messages.success(request, "Post " + post_title + " deleted!")
    return redirect('main-home')


def delete_user(request, pk):
    user = MyUser.objects.get(id=request.session.get("usr_id"))
    user_to_delete = MyUser.objects.get(id=pk)
    username = user_to_delete.username
    user_to_delete.delete()
    messages.success(request, "User " + username + " deleted!")
    return redirect('my-admin')


def update_post(request, pk):
    post_to_update = Post.objects.filter(id=pk).first()
    domains = PostDomain.objects.all()
    types = PostType.objects.all()
    if request.method == 'POST':
        user = MyUser.objects.get(id=request.session.get("usr_id"))
        post_to_update = Post.objects.filter(id=pk).first()
        title = request.POST.get('title')
        type = request.POST.get('type')
        domain = request.POST.get('domain')
        description = request.POST.get('description')
        Post.objects.filter(id=pk).update(title=title,
                                          description=description,
                                          type=type, author=user,
                                          domain=domain)
        messages.success(request, "Post " + post_to_update.title + " updated!")
        return redirect('main-home')

    return render(request, "users/new_update_post.html", {'post': post_to_update, 'domains':domains, 'types':types})


def update_profile(request, pk):
    user = MyUser.objects.get(id=request.session.get("usr_id"))

    if request.method == 'POST':
        print("post --- !")
        # user_to_update = MyUser.objects.filter(id=pk).first()
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # image = request.POST.get('image')
        setattr(user, 'username', username)
        setattr(user, 'email', email)
        setattr(user, 'password', password)

        if 'image' in request.FILES:
            if request.FILES['image']:
                image = request.FILES['image']
                # extension = image.name.split(".")[-1]
                filepath = "users/" + image.name
                fs = FileSystemStorage()
                filename = fs.save(filepath, image)
                uploaded_file_url = fs.url(filename)
                # setattr(user, 'img', filepath)
                user.img = filepath
        # setattr(user, 'img', image)

        user.save()
        # MyUser.objects.filter(id=pk).update(username = username, email = email)
        messages.success(request, "Account updated!")
        return redirect('profile', user.id)

    return render(request, "users/update_profile.html")


def my_admin(request):
    user = MyUser.objects.get(id=request.session.get("usr_id"))
    users = MyUser.objects.all()
    return render(request, "users/my_admin.html", {'users': users})

def manage_types_domains(request):
    domains = PostDomain.objects.all()
    types = PostType.objects.all()
    context = {'domains':domains, 'types':types}

    return render(request, "users/manage_types_domains.html", context)

def create_domain(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if PostDomain.objects.filter(choices = title).exists():
            messages.success(request, "Domain already exists!")
            return redirect('manage-types-domains')
        domain = PostDomain(choices =  title)
        domain.save()
        messages.success(request, "Domain " + domain.choices + " created!")
        return redirect('manage-types-domains')

    return render(request, "users/create_domain.html" )

def create_type(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if PostType.objects.filter(choices = title).exists():
            messages.success(request, "Type already exists!")
            return redirect('manage-types-domains')
        type = PostType(choices =  title)
        type.save()
        messages.success(request, "Type " + type.choices + " created!")
        return redirect('manage-types-domains')

    return render(request, "users/create_type.html" )

def delete_domain(request, pk):
    domain_to_delete = PostDomain.objects.filter(id=pk).first()
    title = domain_to_delete.choices
    posts = Post.objects.all()
    for post in posts:
        if post.domain == title:
            post.domain = 'domain_deleted'
            post.save()
    domain_to_delete.delete()
    messages.success(request, "Domain " + title + " deleted!")
    return redirect('manage-types-domains')

def delete_type(request, pk):
    type_to_delete = PostType.objects.filter(id=pk).first()
    title = type_to_delete.choices
    posts = Post.objects.all()
    for post in posts:
        if post.type == title:
            post.type = 'type_deleted'
            post.save()
    type_to_delete.delete()
    messages.success(request, "Type " + title + " deleted!")
    return redirect('manage-types-domains')

def update_domain(request, pk):

    domain = PostDomain.objects.filter(id=pk).first()
    posts = Post.objects.all()

    if request.method == 'POST':
        print("post --- !")
        # user_to_update = MyUser.objects.filter(id=pk).first()
        title = request.POST.get('title')

        if PostDomain.objects.filter(choices = title).exists():
            messages.success(request, "Domain already exists!")
            return redirect('manage-types-domains')

        for post in posts:
            if post.domain == domain.choices:
                post.domain = title
                post.save()

        # image = request.POST.get('image')
        #setattr(domain, 'choices', title)
        domain.choices = title
        domain.save()





        # MyUser.objects.filter(id=pk).update(username = username, email = email)
        messages.success(request, "Domain updated!")
        return redirect('manage-types-domains')

    return render(request, "users/update_domain.html", {'domain':domain})

def update_type(request, pk):

    type = PostType.objects.filter(id=pk).first()
    posts = Post.objects.all()

    if request.method == 'POST':

        # user_to_update = MyUser.objects.filter(id=pk).first()
        title = request.POST.get('title')
        if PostType.objects.filter(choices = title).exists():
            messages.success(request, "Type already exists!")
            return redirect('manage-types-domains')
        for post in posts:
            if post.type == type.choices:
                post.type = title
                post.save()

        # image = request.POST.get('image')
        #setattr(type, 'choices', title)
        type.choices = title
        type.save()

        messages.success(request, "Type updated!")
        return redirect('manage-types-domains')

    return render(request, "users/update_type.html", {'type':type})