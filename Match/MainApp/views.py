from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt
from .models import User
from .models import Hobby

# Create your views here.

# Render the log in page
def index(req):
    return render(req, 'MainApp/index.html')

@csrf_exempt
def register(req):
    if req.method == 'GET':
        hobbyList = Hobby.objects.all().values('hobbyName', 'hobbyInfo')

        return render(req, 'MainApp/register.html', { 'hobbyList': hobbyList })
    else:
        raise Http404("Something went wrong !")

@csrf_exempt
def newUser(req):
    if req.method == 'POST':
        firstName = req.POST['fName']
        lastName = req.POST['lName']
        age = req.POST['age']
        dob = req.POST['dob']
        gender = req.POST['gender']
        email = req.POST['email']
        password = req.POST['pwd']
        hobbies = req.POST.getlist('hobbies[]')

        for hobby in hobbies:
            print(hobby)

        hobbyList = Hobby.objects.all().values('hobbyName', 'hobbyInfo')

        return render(req, 'MainApp/register.html', { 'hobbyList': hobbies })
    else:
        raise Http404('Something went wrong')
