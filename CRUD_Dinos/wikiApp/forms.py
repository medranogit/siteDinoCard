# wikiApp/forms.py

from django import forms  # Importa o módulo de formulários do Django
from django.contrib.auth.forms import UserCreationForm  # Importa o formulário de criação de usuário padrão do Django
from django.contrib.auth.models import User  # Importa o modelo User do Django
from .models import UserProfile  # Importa o modelo UserProfile definido na aplicação

class UserRegistrationForm(UserCreationForm):
    # Cria um formulário personalizado para registro de usuário, estendendo o UserCreationForm

    bio = forms.CharField(max_length=500, required=False, widget=forms.Textarea(attrs={'rows': 3}))
    # Campo adicional para biografia, com tamanho máximo de 500 caracteres e um widget de área de texto

    location = forms.CharField(max_length=30, required=False)
    # Campo adicional para localização, com tamanho máximo de 30 caracteres

    age = forms.IntegerField()  # Campo de idade adicionado


    class Meta:
        model = User  # Define o modelo base para este formulário como User
        fields = ['username', 'password1', 'password2','age', 'bio', 'location']
        # Define os campos que serão exibidos no formulário
