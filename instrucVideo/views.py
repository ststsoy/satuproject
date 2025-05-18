from django.shortcuts import render
from django.http import HttpResponse
from  .models import*

# Create your views here.

def home(request):
	post = InstrucVideo.objects.all()
	return render(request,'instrucVideo/index.html',{'post':post})
