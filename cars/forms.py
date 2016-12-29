from django import forms
from .models import Car

class PostForm(forms.ModelForm):
	class Meta:
		model=Car
		fields=['Model','Price','image_url','Instance','Colors','Varients','Engine']