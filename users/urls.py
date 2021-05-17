from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('login/', views.login_user.as_view(), name='login'),
    path('logout/', views.logout_user.as_view(), name='logout'),
    path('status/', views.status.as_view(), name='status'),
    path('search/', views.search_user, name='search_user'),
    path('token/',obtain_auth_token)
]
