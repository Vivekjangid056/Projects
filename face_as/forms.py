from django import forms
from django.forms import ModelForm
from face_as.models import student
from django.core import validators

class ProfileForm(forms.ModelForm):

    class Meta:
        model = student
        fields = ['name','roll_number','gender','phone','email','branch','sem','subject','image','shift']
        labels ={'sem':'Semester'}
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Name'}),
            'roll_number':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Roll Number'}),
            # 'gender':forms.ChoiceField(forms.Select,choices=gender_choice),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email Address'}),
            'phone':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Your contect Number'}),
            'branch':forms.TextInput(attrs={'class':'form-control'}),
            'sem':forms.TextInput(attrs={'class':'form-control'}),
            'subject':forms.TextInput(attrs={'class':'form-control'}),
        }
        

         

    # name=forms.CharField()
    # roll_number=forms.IntegerField()
    # gender_choice =(
    # ('male','male'),
    # ('female','female')
    # )
    # gender=forms.CharField()
    # email=forms.EmailField()
    # phone=forms.IntegerField()
    # branch=forms.CharField()
    # sem=forms.CharField()
    # image=forms.ImageField(required=False)

    