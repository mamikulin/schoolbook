from .models import book
from django.forms import ModelForm, TextInput, Textarea
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "last_name", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        if user.last_name[0] == '@':
            user.last_name = '{}'.format(user.last_name)[1:]
        else:
            pass
        if commit:
            user.save()
        return user
        

class bookform(ModelForm):

    class Meta:
        model = book
        fields = ['owner','ownerscontact', 'name', 'price', 'description', 'author', 'year', 'publisher', 'image', 'status']
        widgets = {
            'owner': TextInput(attrs={
            }),
            'ownerscontact': TextInput(attrs={
            }),
            'status': TextInput(attrs={'placeholder': "Введите status"
            }),
            'name': TextInput(attrs={'placeholder': "название"
            }),
            'price': TextInput(attrs={'placeholder': "цена"
            }),
            'description': Textarea(attrs={'placeholder': "описание"
            }),
            'author': TextInput(attrs={'placeholder': "автор"
            }),
            'year': TextInput(attrs={'placeholder': "год издания"
            }),
            'publisher': TextInput(attrs={'placeholder': "изатель"
            }),


        }
