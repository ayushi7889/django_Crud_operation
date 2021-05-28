from django import forms
from .models import Crud

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Crud
        fields = ('fullname','emp_code','mobile','position')
        labels = {
            'fullname':'Full Name',
            'emp_code':'EMP. code'
        }

    def __init__(self,*args,**kwargs):
        super(EmployeeForm,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label = 'Select'
        self.fields['emp_code'].required = False