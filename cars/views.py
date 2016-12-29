from django.shortcuts import render,get_object_or_404
from .models import Car
from django.http import HttpResponse
import json
from .forms import PostForm

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



