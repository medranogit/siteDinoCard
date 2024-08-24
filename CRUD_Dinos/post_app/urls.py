from django.urls import path  # Importa a função 'path' do Django, usada para definir padrões de URL.
from . import views  # Importa o módulo 'views' do aplicativo atual, onde estão definidas as views.

urlpatterns = [
    path('', views.post_list, name='post-list'),  # Define uma URL padrão ('/') que mapeia para a view 'post_list'.
                                                  # O nome 'post-list' é uma referência para essa URL, que pode ser usada em templates e em outros lugares no código.
    
    path('post-create', views.post_create, name='post-create'),  # Define uma URL ('/post-create') que mapeia para a view 'post_create'.
                                                                 # O nome 'post-create' permite referenciar essa URL facilmente em templates ou em redirecionamentos.
    
#     path('post-detail/<int:id>/', views.post_detail, name='post-detail'),  # Define uma URL ('/post-detail/<int:id>/') que mapeia para a view 'post_detail'.
#                                                                            # O <int:id> captura um número inteiro da URL e o passa como argumento para a view.
#                                                                            # O nome 'post-detail' permite referenciar essa URL em templates e em outros lugares no código.
]
