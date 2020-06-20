from django.shortcuts import render, Http404, HttpResponseRedirect, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Aktuality, Dite, Dospely, Krouzek, KontaktInfo, PlatebniInfo, LekceDospeli
from .forms import DiteForm, DospelyForm, KontaktInfoForm
from django.urls import reverse

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
        "aktuality": Aktuality.objects.filter(typ_aktualit='children').all(),
        "courses": Krouzek.objects.all()
    }

    for course in context.get('courses'):
        course.den_cs, course.den_en = day_to_text_dict(course.den)
        #print(course.den)
        #print(course.den_cs)
        #print(course.den_en)
        #print("...............")

    # for course in context.get('courses'):
    #     children = course.zaci_krouzku.all()
    #     print(children)

    return render(request, "keramika_ostrovni_web/children.html", context)


def day_to_text_dict(course_day):
    course_day_cs = ""
    course_day_en = ""
    if course_day == "mon":
        course_day_cs = "pondělí"
        course_day_en = "monday"
    if course_day == "tue":
        course_day_cs = "úterý"
        course_day_en = "tuesday"
    if course_day == "wed":
        course_day_cs = "středa"
        course_day_en = "wednesday"
    if course_day == "thu":
        course_day_cs = "čtvrtek"
        course_day_en = "thursday"
    if course_day == "fri":
        course_day_cs = "pátek"
        course_day_en = "friday"
    if course_day == "sat":
        course_day_cs = "sobota"
        course_day_en = "saturday"
    if course_day == "sun":
        course_day_cs = "neděle"
        course_day_en = "sunday"

    return course_day_cs, course_day_en


def children_sign_up(request):
    context = {"username": request.user.username}
    print(request.method)
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


def account_info(request):
    print("+++++----+++++")
    if request.user.is_anonymous:
        print("is anonym")
        raise Http404("Prosíme, nejprve se přihlašte :)")
    print(request)
    if request.method == 'GET':
        username = request.user.username

        children = request.user.deti.all()
        form = DiteForm()  # create blank instance of the form and send it to the user

        adults = request.user.dospeli.all()
        contact_info = request.user.kontakt_info.all()  # todo clean code
        payment_info = request.user.platebni_info.all()
        if len(contact_info) > 0:
            contact_info = contact_info[0]
        if len(payment_info) > 0:
            payment_info = payment_info[0]
        print(contact_info)
        print(payment_info)

        context = {"username": username, 'form': form, "children": children, "dospeli": adults,
                   "platebni_info": payment_info, "kontakt_info": contact_info}
    return render(request, "keramika_ostrovni_web/account_info.html", context)


def account_info_edit(request):
    if request.user.is_anonymous:
        print("is anonym")
        raise Http404("Prosíme, nejprve se přihlašte :)")
    username = request.user.username
    try:
        print(request.user.kontakt_info.all())
        contact_info = request.user.kontakt_info.all()[0]  # todo make it nicer
        payment_info = request.user.platebni_info.all()[0]
    except KontaktInfo.DoesNotExist or PlatebniInfo.DoesNotExist:
        raise Http404("KontaktInfo or PlatebniInfo does not exist, sorries")
    except IndexError:
        contact_info = KontaktInfo(username=request.user)
        contact_info.save()
        payment_info = PlatebniInfo(username=request.user)
        payment_info.save()

    if request.method == 'GET':
        form_contact = KontaktInfoForm()
        if len(contact_info.email) == 0:  # if empty email assume username is email
            try:
                contact_info.email = username
                contact_info.save()
            except:
                print("not valid email really...")
        context = {"username": username, 'form_contact': form_contact, 'contact_info': contact_info,
                   'payment_info': payment_info}
        return render(request, "keramika_ostrovni_web/account_info_edit.html", context)
    if request.method == 'POST':
        form_contact = KontaktInfoForm(data=request.POST)  # data validation
        if ((request.POST.get('input_button', "") == "Uložit změny") or (
                request.POST.get('input_button', "") == "Save changes")):
            if form_contact.is_valid():

                contact_info.jmeno = request.POST.get('jmeno', "")
                contact_info.prijmeni = request.POST.get('prijmeni', "")
                contact_info.telefoni_cislo = request.POST.get('telefoni_cislo', "")
                contact_info.email = request.POST.get('email', "")
                contact_info.save()
                return redirect('account_info')
            else:
                print("form not valid")
                print(form_contact.error_messages)
                context = {"username": username, 'form_contact': form_contact, 'contact_info': contact_info,
                           'payment_info': payment_info}
                return render(request, "keramika_ostrovni_web/account_info_edit.html", context)

        if (request.POST.get('input_button', "") == "Storno"):
            return redirect('account_info')


def child_edit(request, child_id):
    if request.user.is_anonymous:
        print("is anonym")
        raise Http404("Prosíme, nejprve se přihlašte :)")
    username = request.user.username
    try:
        user_children = request.user.deti.all()
        print(user_children)
        child = user_children.get(pk=child_id)
    except Dite.DoesNotExist:
        raise Http404("Dite does not exist, sorries")

    if request.method == 'GET':
        form = DiteForm()
        context = {"username": username, 'form': form, "child": child}
        return render(request, "keramika_ostrovni_web/child_edit.html", context)
    if request.method == 'POST':
        form = DiteForm(data=request.POST)  # data validation
        if ((request.POST.get('input_button', "") == "Uložit změny") or (
                request.POST.get('input_button', "") == "Save changes")):
            if form.is_valid():
                print(child)
                child.jmeno = request.POST.get('jmeno', "")
                child.prijmeni = request.POST.get('prijmeni', "")
                child.rocnik = request.POST.get('rocnik', "")
                child.paralelka = request.POST.get('paralelka', "")
                child.ve_skolnim_roce = request.POST.get('ve_skolnim_roce', "")
                print("new")
                print(child)
                child.save()
                print(Dite.objects.all())
                return redirect('account_info')
            else:
                print("form not valid")
                print(form.error_messages)
                return render(request, "keramika_ostrovni_web/child_edit.html",
                              {"username": username, 'form': form, "child": child})
        if (request.POST.get('input_button', "") == "Storno"):
            return redirect('account_info')
        if ((request.POST.get('input_button', "") == "Smazat záznam") or (
                request.POST.get('input_button', "") == "Delete entry")):
            child.delete()
            return redirect('account_info')


def child_add_new(request):
    if request.user.is_anonymous:
        print("is anonym")
        raise Http404("Prosíme, nejprve se přihlašte :)")
    username = request.user.username

    if request.method == 'GET':
        form = DiteForm()
        context = {"username": username, 'form': form}
        return render(request, "keramika_ostrovni_web/children_add_new.html", context)
    if request.method == 'POST':
        form = DiteForm(data=request.POST)  # data validation
        if ((request.POST.get('input_button', "") == "Uložit") or (request.POST.get('input_button', "") == "Save")):
            if form.is_valid():
                jmeno = request.POST.get('jmeno', "")
                prijmeni = request.POST.get('prijmeni', "")
                rocnik = request.POST.get('rocnik', "")
                paralelka = request.POST.get('paralelka', "")
                ve_skolnim_roce = request.POST.get('ve_skolnim_roce', "")
                print("new")
                child = Dite(username=request.user, jmeno=jmeno, prijmeni=prijmeni, rocnik=rocnik, paralelka=paralelka,
                             ve_skolnim_roce=ve_skolnim_roce)
                print(child)
                child.save()
                print(Dite.objects.all())
                return redirect('account_info')
            else:
                print("form not valid")
                print(form.error_messages)
                return render(request, "keramika_ostrovni_web/children_add_new.html",
                              {"username": username, 'form': form})
        if (request.POST.get('input_button', "") == "Storno"):
            return redirect('account_info')


def adult_edit(request, adult_id):
    if request.user.is_anonymous:
        print("is anonym")
        raise Http404("Prosíme, nejprve se přihlašte :)")
    username = request.user.username
    try:
        user_adults = request.user.dospeli.all()
        print(user_adults)
        adult = user_adults.get(pk=adult_id)
    except Dospely.DoesNotExist:
        raise Http404("Dospely does not exist, sorries")

    if request.method == 'GET':
        form = DospelyForm()
        context = {"username": username, 'form': form, "adult": adult}
        return render(request, "keramika_ostrovni_web/adult_edit.html", context)
    if request.method == 'POST':
        form = DospelyForm(data=request.POST)  # data validation
        if ((request.POST.get('input_button', "") == "Uložit změny") or (
                request.POST.get('input_button', "") == "Save changes")):
            if form.is_valid():
                print(adult)
                adult.jmeno = request.POST.get('jmeno', "")
                adult.prijmeni = request.POST.get('prijmeni', "")
                print("new")
                print(adult)
                adult.save()
                print(Dospely.objects.all())
                return redirect('account_info')
            else:
                print("form not valid")
                print(form.error_messages)
                return render(request, "keramika_ostrovni_web/adult_edit.html",
                              {"username": username, 'form': form, "adult": adult})
        if (request.POST.get('input_button', "") == "Storno"):
            return redirect('account_info')
        if ((request.POST.get('input_button', "") == "Smazat záznam") or (
                request.POST.get('input_button', "") == "Delete entry")):
            adult.delete()
            return redirect('account_info')


def adult_add_new(request):
    if request.user.is_anonymous:
        print("is anonym")
        raise Http404("Prosíme, nejprve se přihlašte :)")
    username = request.user.username

    if request.method == 'GET':
        form = DospelyForm()
        context = {"username": username, 'form': form}
        return render(request, "keramika_ostrovni_web/adult_add_new.html", context)
    if request.method == 'POST':
        form = DospelyForm(data=request.POST)  # data validation
        if ((request.POST.get('input_button', "") == "Uložit") or (request.POST.get('input_button', "") == "Save")):
            if form.is_valid():
                jmeno = request.POST.get('jmeno', "")
                prijmeni = request.POST.get('prijmeni', "")
                print("new")
                dospely = Dospely(username=request.user, jmeno=jmeno, prijmeni=prijmeni)
                print(dospely)
                dospely.save()
                print(Dospely.objects.all())
                return redirect('account_info')
            else:
                print("form not valid")
                print(form.error_messages)
                return render(request, "keramika_ostrovni_web/children_add_new.html",
                              {"username": username, 'form': form})
        if (request.POST.get('input_button', "") == "Storno"):
            return redirect('account_info')


def children_sign_into_classes(request):
    if request.user.is_anonymous:
        print("is anonym")
        raise Http404("Prosíme, nejprve se přihlašte :)")
    print(request.method)
    if request.method == 'GET':
        children = request.user.deti.all()
        context = {
            "username": request.user.username,
            "courses": Krouzek.objects.all().order_by('cislo_krouzku'),
            "children": children
        }

        for course in context.get('courses'):
            course.den_cs, course.den_en = day_to_text_dict(course.den)
            #print(course.den)
            ##print(course.den_cs)
            #print(course.den_en)
            #print("...............")
            #print(course.zaci_krouzku.all())
            #print(len(course.zaci_krouzku.all()))
            course.free_spots = course.max_kapacita_krouzku - len(course.zaci_krouzku.all())

            if course.free_spots <= 0:
                course.is_full = True
            else:
                course.is_full = False
            #print(course.free_spots)
        return render(request, "keramika_ostrovni_web/children_sign_into_classes.html", context)


def sign_up_child(request):
    try:
        child_id = int(request.POST["child"])
        child = Dite.objects.get(pk=child_id)
        print(child_id)
        print(child.jmeno)
        print(request.POST)
        course_id = int(request.POST["sign_in_button"])
        course = Krouzek.objects.get(pk=course_id)
        print(course)
        #child.krouzky.add()
        print("-*-*-*-*-*-*")
    except:
        raise Http404("something went terribly wrong >{")

    child.krouzky.add(course)
    return HttpResponseRedirect(reverse("children_sign_into_classes", args=()))

def children_logout(request):
    if request.user.is_anonymous:
        print("is anonym")
        raise Http404("Prosíme, nejprve se přihlašte :)")
    print(request.method)
    if request.method == 'POST':
        logout(request)
        return redirect('children')


def adults(request):
    context = {
        "username": request.user.username,
        "aktuality": Aktuality.objects.filter(typ_aktualit='adults').all(),
        "courses": LekceDospeli.objects.all()
    }
    for course in context.get('courses'):
        course.den_cs, course.den_en = day_to_text_dict(course.den)
        #print(course.den)
        #print(course.den_cs)
        #print(course.den_en)
        #print("...............")

    return render(request, "keramika_ostrovni_web/adults.html", context)


def teachers(request):
    context = {
        "username": request.user.username
    }
    return render(request, "keramika_ostrovni_web/teachers.html", context)
