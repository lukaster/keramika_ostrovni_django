from django.shortcuts import render, Http404, HttpResponseRedirect, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Aktuality


# Create your views here.
def index(request):
    # return HttpResponse("hello there")
    print(request.user.username)
    context = {
        "username": request.user.username
    }
    return render(request, "keramika_ostrovni_web/index.html", context)


def children(request):
    context = {
        "username": request.user.username,
        "aktuality": Aktuality.objects.filter(typ_aktualit='children').all()
    }
    return render(request, "keramika_ostrovni_web/children.html", context)


def children_sign_up(request):
    context = {"username": request.user.username}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # data validation
        if form.is_valid():
            user = form.save()  # saves data to db
            login(request, user)
            return redirect('children')
        else:
            return render(request, "keramika_ostrovni_web/children_sign_up.html",
                          {"username": request.user.username, 'form': form})

    if request.method == 'GET':
        form = UserCreationForm()  # create blank instance of the form and send it to the user
        context = {"username": request.user.username, 'form': form}
    return render(request, "keramika_ostrovni_web/children_sign_up.html", context)


def children_login(request):
    context = {"username": request.user.username}
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)  # data validation
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('children')
        else:
            return render(request, "keramika_ostrovni_web/children_login.html",
                          {"username": request.user.username, 'form': form})

    if request.method == 'GET':
        form = AuthenticationForm()  # create blank instance of the form and send it to the user
        context = {"username": request.user.username, 'form': form}
    return render(request, "keramika_ostrovni_web/children_login.html", context)


def children_logout(request):
    print(request.method)
    if request.method == 'POST':
        logout(request)
        return redirect('children')



def adults(request):
    context = {
        "username": request.user.username,
        "aktuality": Aktuality.objects.filter(typ_aktualit='adults').all()
    }
    return render(request, "keramika_ostrovni_web/adults.html", context)


def teachers(request):
    context = {
        "username": request.user.username
    }
    return render(request, "keramika_ostrovni_web/teachers.html", context)
