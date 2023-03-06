from django.urls import path
from . import views

# http://127.0.0.1:8000/client     = anasayfa
# http://127.0.0.1:8000/clien/home = anasayfa
# http://127.0.0.1:8000/client/makaleler = makaleleri göster





urlpatterns = [
    path('',views.home),
    path('anasayfa',views.home),
    path('makaleler',views.articles),
]
