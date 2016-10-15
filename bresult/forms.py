from django import forms
from bresult.models import Result

class ResultForm(forms.ModelForm):
	class Meta:
		model = Result
		fields = ('number', 'result',)
