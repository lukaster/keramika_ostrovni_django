
from django.shortcuts import render, Http404, HttpResponseRedirect,HttpResponse
# Create your views here.
def index(request):
    #return HttpResponse("hello there")
    context={

    }
    return render(request,"keramika_ostrovni_web/index.html",context)

def children(request):
    #return HttpResponse("hello there")
    context={

    }
    return render(request,"keramika_ostrovni_web/children.html",context)

def adults(request):
    #return HttpResponse("hello there")
    context={

    }
    return render(request,"keramika_ostrovni_web/adults.html",context)


def teachers(request):
    #return HttpResponse("hello there")
    context={

    }
    return render(request,"keramika_ostrovni_web/teachers.html",context)
