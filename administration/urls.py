from django.urls import path
from .views import LoginView

# url partterns
urlpatterns = [
    path('login',LoginView.as_view(),name='login'),

]

