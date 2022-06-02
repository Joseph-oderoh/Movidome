from . import views
from django.urls import path,re_path


urlpatterns = [
    path('', views.homepage, name='landing'),
    # path('profile/(?P<username>[-_\w.]+)/', views.profile, name='profile'),
    
    path('user/<user_id>', views.profile, name='profile'),
]