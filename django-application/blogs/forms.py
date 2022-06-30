from django import forms
from .models import Contact, Post, Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')

# Creating Register Form
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

# Creating Contact form
class ContactForm(ModelForm):
	class Meta:
		model = Contact
		fields = '__all__'