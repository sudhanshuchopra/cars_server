from django.shortcuts import render,get_object_or_404
from .models import Car
from django.http import HttpResponse
import json
from .forms import PostForm
from random import randint
# Create your views here.
def get_content(request):
	p=request.GET.get('instance','')
	if(p==''):
		p='14'
	k=get_object_or_404(Car,Instance=p)
	context={
	'Model':k.Model,
	'Price':k.Price,
	'image_url':k.image_url,
	'Colors':k.Colors,
	'Varients':k.Varients,
	'Engine':k.Engine,
	}
	#context=
	return HttpResponse(json.dumps(context), content_type="application/json")

def post_content(request):
	if(request.method=='GET'):
		form=PostForm()
		context={
		"form":form
		}
		return render(request,"cars/post_form.html",context)
	if(request.method=='POST'):
		form=PostForm(request.POST)
		if(form.is_valid()):
			f=form.save(commit=False)
			f.save()
			return HttpResponse('OK')
		else:
			return render(request,"cars/post_form.html",{"form":form})

def need_help(request):
	k=request.GET.get('val','')
	emp_list=['akash','varun','gagan','arun','shivam','mahesh','suresh']
	if(k=='y'):
		p=randint(0,6)
		v=emp_list[p]
		response_text="Mr "+emp_list[p] +" "+"will be there in a minute  to help you!!"
		context={
		"response_text":response_text
		}
		return HttpResponse(json.dumps(context),content_type="application/json")
	else:
		context={
		"response_text":"If you need any help, contact us anytime"
		}
		return HttpResponse(json.dumps(context),content_type="application/json")






