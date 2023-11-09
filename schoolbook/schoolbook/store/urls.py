from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *




app_name = "store"

urlpatterns = [

    path('', views.index, name='home'),
    path("register", views.register_request, name="register"),
    path('createanapplication', views.createanapplication, name='create'),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("user/", views.user, name = "user"),
    path("card/", views.goodcard, name = "card"),
    path('card/delete/<int:id>', views.delete, name='delete'),
    path('user/delete/<int:id>', views.delete, name='delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

