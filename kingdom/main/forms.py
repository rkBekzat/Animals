from .models import Animal
from django.forms import ModelForm, TextInput, Textarea

class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = ['avatar', 'bio', 'firstname', 'lastname', 'title']

        widgets = {
            'avatar' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Link to the photo'
            }),
            'bio' : Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : 'Bio'
            }),
            'firstname' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'firstname'
            }),
            'lastname' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'lastname'
            }),
            'title' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'title'
            }),
        }