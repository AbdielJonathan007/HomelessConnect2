from django.urls import path
from .views  import rag_query_view, home
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page route
    path('chatbot/chat/', views.rag_query_view, name='rag_query'),  # Chatbot query route
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

