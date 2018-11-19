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
        h = QueryDict(req.body)
        firstName = req.POST['fName']
        lastName = req.POST['lName']
        age = req.POST['age']
        dob = req.POST['dob']
        gender = req.POST['gender']
        email = req.POST['email']
        password = req.POST['pwd']
        hobbies = req.POST.getlist('hobbies[]')

        #print(firstName)
        print(hobbies)

        #profilePic to be resolved still
        user = User(firstName=firstName, lastName=lastName, age=age, dob=dob, gender=gender, email=email, password=password)
        user.save()

        for hobbyName in hobbies:
            hobby = Hobby.objects.get(pk=hobbyName)
            user.hobbies.add(hobby)
            print(hobby.hobbyName)

        #hobbyList = Hobby.objects.all().values('hobbyName', 'hobbyInfo')

        users = list(User.objects.all().values('firstName', 'lastName', 'age', 'dob', 'gender', 'email', 'password', 'hobbies'))

        #return render(req, 'MainApp/register.html', { 'hobbyList': hobbies })

        return JsonResponse(users, safe=False)
    else:
        raise Http404('Something went wrong')
