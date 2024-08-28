from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import UserRegistrationForm  # Importa o formulário personalizado de registro
from .models import UserProfile  # Importa o modelo UserProfile definido na aplicação

# Views baseadas em funções (Function-Based Views - FBVs)
def index(request):
    """View para renderizar a página inicial."""
    return render(request, 'myApp/index.html')

def teste(request):
    """View para renderizar a página de teste."""
    return render(request, 'myApp/teste.html')

@login_required
def dashboard(request):
    template_name = 'myApp/dashboard.html'

    # Obtém o perfil do usuário logado
    user_profile = UserProfile.objects.get(user=request.user)

    # Passa as informações do perfil para o template
    data = {
        'bio': user_profile.bio,
        'location': user_profile.location,
        'age': user_profile.age
    }


    return render(request, template_name, data)

def registro(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)  # Cria uma instância do formulário com os dados POST
        if form.is_valid():
            user = form.save()  # Salva o usuário e retorna a instância do usuário criado
            # Criação do UserProfile para o novo usuário
            bio = form.cleaned_data.get('bio')  # Obtém o valor do campo 'bio' do formulário
            location = form.cleaned_data.get('location')  # Obtém o valor do campo 'location' do formulário
            age = form.cleaned_data.get('age')

            UserProfile.objects.create(user=user, bio=bio, location=location, age=age)
            # Cria um perfil de usuário associado ao novo usuário
            
            messages.success(request, 'Sua conta foi criada com sucesso! Você já pode fazer login.')
            # Adiciona uma mensagem de sucesso à solicitação
            
            return redirect('login')  # Redireciona o usuário para a página de login
    else:
        form = UserRegistrationForm()  # Cria uma instância vazia do formulário
    return render(request, 'myApp/registro.html', {'form': form})
    # Renderiza o template de registro com o formulário

# Define uma view personalizada para o login
class CustomLoginView(auth_views.LoginView):
    """
    Esta view personalizada de login redireciona o usuário para o dashboard
    se ele já estiver autenticado, evitando que usuários logados vejam a 
    página de login novamente.
    """

    # Especifica o template que será usado para renderizar a página de login
    template_name = 'myApp/login.html'

    # Sobrescreve o método dispatch, que é chamado antes de qualquer outro método
    def dispatch(self, request, *args, **kwargs):
        # Verifica se o usuário está autenticado
        if request.user.is_authenticated:
            # Se o usuário estiver autenticado, redireciona para o dashboard
            return redirect('dashboard')
        # Se o usuário não estiver autenticado, prossegue com o fluxo normal da view de login
        return super().dispatch(request, *args, **kwargs)