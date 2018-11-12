from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User

# Create your views here.

# Render the log in page
def index(req):
    return render(req, 'MainApp/index.html')

@csrf_exempt
def register(req):
    if req.method == 'GET':
        return render(req, 'MainApp/register.html')
    else:
        raise Http404("Something went wrong !")

@csrf_exempt
def validation(req):
    if req.method == 'POST':
        firstName = req.POST['firstName']
        lastName = req.POST['lastName']
        age = req.POST['age']
        dob = req.POST['dob']
        gender = req.POST['gender']
        email = req.POST['email']
        password = req.POST['password']
        profilePic = req.POST['profilePic']

        user = User(firstName=firstName, lastName=lastName, age=age, dob=dob, gender=gender, email=email, password=password, profilePic=profilePic)
        user.save()

        users = list(User.objects.all())

        return JsonResponse(users, safe=False)
    else:
        raise Http404('Something went wrong')
