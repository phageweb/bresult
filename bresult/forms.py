from django import forms
from bresult.models import  Pair

class PairForm(forms.ModelForm):
	class Meta:
		model = Pair
		fields = ('id',)

class PairForm(forms.ModelForm):
	class Meta:
		model = Pair
		fields = ('id','person1','person2')
