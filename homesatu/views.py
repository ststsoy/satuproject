from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home(request):
	post=Homesatu.objects.all()
	cater=Category.objects.all()
	return render(request,'homesatu/base.html',{'post':post,'cater':cater})
	#return HttpResponse("Казак, который отбил дрон головой.Вы помните парня-казака, который использовал голову, чтобы сбить дрон?Его зовут Михаил, ему 33 года. Он потомственный казак из Воронежской области и воевал на Донбассе в 2014-2015 годах. В июле этого года он ушёл добровольцем-штурмовиком на специальную военную операцию.В начале августа на Харьковском направлении Михаил мог погибнуть от атаки дрона ВСУ, но ему удалось отбить его головой. Он был ранен, несмотря на каску: получил рассечение, а также осколки рядом с позвоночником и в голени. При этом, несмотря на шок")

# Create your views here.
def homesatu(request,homesatu_id):
	post=Homesatu.objects.get(id=homesatu_id)
	inv=Insvid.objects.filter(podcast=homesatu_id)
	return render(request,'homesatu/invid.html',{'post':post,'inv':inv})


def cat(request,category_id):
	
	post=Homesatu.objects.filter(category_homesatu=category_id)
	cater=Category.objects.filter(id=category_id)
	return render(request,'homesatu/cat.html',{'cater':cater,'post':post})
	
def category(request):
	cater=Category.objects.all()
	return render(request,'homesatu/category.html',{'cater':cater})	