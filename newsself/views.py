from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect ,get_object_or_404
from newsself.models import Newsself,Addphoto
from newsself.forms import AddphotoForm
from django.views.decorators.csrf import csrf_protect


# Create your views here.

def newsself(request):
	news=Newsself.objects.all()
	addph = Addphoto.objects.all()
	form = AddphotoForm()

	return render(request,'newsself/newsself.html',{'news':news,'addph':addph,'form':form})


def addphoto(request):

	if request.method=='POST':
		form =AddphotoForm(request.POST,request.FILES)
		if form.is_valid():
		
				form.save()
				return redirect('newsself')
			

	else:
		form =AddphotoForm()
	return render(request,'newsself/newsself.html',{'form':form})