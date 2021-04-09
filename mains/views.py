from django.shortcuts import render, redirect
from .models import Post, PostType, PostDomain
from users.models import MyUser
from users.forms import  FilterPosts

last_type = 'not_initialized'
last_domain = 'not_initialized'

# Create your views here.
def home(request):
    global last_type
    global last_domain
    if last_type != 'not_initialized':
        type = last_type
    else:
        type = 'None'

    if last_domain != 'not_initialized':
        domain = last_domain
    else:
        domain = 'None'
    if "usr_id" in request.session:
        user = MyUser.objects.get(id = request.session.get("usr_id"))
    else:
        user = None

    posts = Post.objects.all()

    if request.method == 'POST':

            type = request.POST.get('type')
            domain = request.POST.get('domain')
            last_type = type
            last_domain = domain
            if type != "None" and domain == "None":
                posts = Post.objects.filter(type = type)
            elif  type == "None" and domain != "None":
                posts = Post.objects.filter(domain=domain)
            elif  type != "None" and domain != "None":
                posts = Post.objects.filter(domain=domain, type = type)
            else:
                posts = Post.objects.all()

    type_choice = PostType.objects.all()
    domain_choice = PostDomain.objects.all()


    context = {
        'posts': posts[::-1],
        'user': user,
        'type':type,
        'domain':domain,
        'type_choice':type_choice,
        'domain_choice':domain_choice
    }

    last_type = 'not_initialized'
    last_domain = 'not_initialized'
    return render(request, 'mains/home.html', context)


