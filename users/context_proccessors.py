from .models import MyUser

def usergetter(request):
    if "usr_id" in request.session:
        varUsr = MyUser.objects.get(id = request.session.get("usr_id"))
        is_logged = True
    else:
        varUsr = None
        is_logged = False
    return  {
        'var_usr' : varUsr,
        'is_logged' : is_logged,
    }