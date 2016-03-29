from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import *
from django.forms import ModelForm
from .forms import *
p=User
# Create your views here.
def getName(request):
	#check if the request post so we need to process the form data
	if request.method=='POST':
		#create the form instance and populate it with data from the request
		form=nameForm(request.POST)
		#check if it's valid
		if form.is_valid():
			#process the data in form.cleand_data

			#redirect to a new URL
			return HttpResponseRedirect('/done/')

	#if any other method we will create blank form
	else:
		form=nameForm()

	return render(request,'appClinic/name.html',{'form':form})

def index(request):
	#return HttpResponse("Welcome to index")
	if request.method=='POST':
		val = request.POST
		if request.POST['login']=='zzz':
		    return HttpResponse("search")
		else:
			return render(request,'appClinic/loginpage.html')
	else:
		return render(request,'appClinic/home.html')

def yourName(request):
	return HttpResponse("your name is "+request.POST.get("yourName", ""))


def addlap(request):
	if(request.method=='POST'):
		labForm = LabForm(request.POST)

		if(labForm.is_valid):
			#create an instanse of user and pass it to labform >>
			#user=myuser()

			labForm.save()

			return HttpResponseRedirect('/done/')

	else:
		labForm = LabForm()

	return render(request,'appClinic/addLap.html',{'form':labForm})


def lapName(request):
	#done added lap
	return HttpResponse("Lap Name "+request.POST.get("name",""))

def login(request):
	if(request.method=='POST'):
		p=User
		form = request.POST
		mail=form['email']
		passwrd=form['password']
		#return HttpResponse(passwrd)
		try:
			user = p.objects.all().get(email=mail,password=passwrd)
			return HttpResponse("User is valid, active and authenticated")
		except :
			return HttpResponse("The username and password were incorrect.")
			#return HttpResponse("User is valid, active and authenticated")
	else:
		return render(request,'appClinic/loginpage.html')
