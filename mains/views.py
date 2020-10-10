from django.shortcuts import render
from .models import Post
from users.models import MyUser


# Create your views here.
def home(request):
    if "usr_id" in request.session:
        user = MyUser.objects.get(id = request.session.get("usr_id"))
    else:
        user = None

    posts = Post.objects.all()
    context = {
        'posts': posts[::-1],
        'user':user,
    }
    return render(request, 'mains/home.html', context)


