from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

# Views baseadas em funções (Function-Based Views - FBVs)
def index(request):
    """View para renderizar a página inicial."""
    return render(request, 'myApp/index.html')

def teste(request):
    """View para renderizar a página de teste."""
    return render(request, 'myApp/teste.html')

@login_required
def dashboard(request):
    """View para renderizar o dashboard. Requer que o usuário esteja logado."""
    return render(request, 'myApp/dashboard.html')

def registro(request):
    """View para processar o registro de um novo usuário."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sua conta foi criada com sucesso! Você já pode fazer login.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'myApp/registro.html', {'form': form})

# Views baseadas em classes (Class-Based Views - CBVs)
class CustomLoginView(auth_views.LoginView):
    """View personalizada para o login, redireciona para o dashboard se o usuário estiver logado."""
    template_name = 'myApp/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)
