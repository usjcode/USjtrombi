from django.urls import path
from .views import TrombiView,HomeView,PageView
from django.conf.urls.static import static

# url partterns
urlpatterns = [
    path('trombinoscope/<str:year>',TrombiView.as_view(),name='trombinoscope'),
    path('trombinoscope/<str:year>/<int:role>',PageView.as_view(),name='trombinoscope'),
    path('',HomeView.as_view(),name='home'),

]

