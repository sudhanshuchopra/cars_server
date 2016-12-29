from django.shortcuts import render,get_object_or_404
from .models import Car
from django.http import HttpResponse
import json

# Create your views here.
def get_content(request):
	p=request.GET.get('instance','')
	if(p==''):
		p='12'
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



