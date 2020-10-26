from django import forms
from . models import Exam,Questions
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class ExamForm(forms.ModelForm):
    class Meta:
        model=Exam
        fields='__all__'
class QuestionsForm(forms.ModelForm):
    class Meta:
        model=Questions
        exclude=['exam']

    def clean(self):
        solution=self.cleaned_data['solution']
        print(solution)
        print(solution=="SS")
        if solution=="SS":
            raise forms.ValidationError("You have to select Solution")
        return self.cleaned_data
class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=200)
    password1 = forms.CharField(max_length=32, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=32, widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
