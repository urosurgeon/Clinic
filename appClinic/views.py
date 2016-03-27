from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import *
from django.forms import ModelForm

from .forms import *

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
	return HttpResponse("Welcome to index")

def yourName(request):
	return HttpResponse("your name is "+request.POST.get("yourName", ""))


def addlap(request):
	if(request.method=='POST'):
		labForm = LabForm(request.POST)

		if(labForm.is_valid):
			#create an instanse of user and pass it to labform >>
			user=myuser()

			labform.save()

			return HttpResponseRedirect('/done/')

	else:
		labForm = LabForm()

	return render(request,'appClinic/addLap.html',{'form':labForm})


def lapName(request):
	#done added lap
	return HttpResponse("Lap Name "+request.POST.get("name",""))