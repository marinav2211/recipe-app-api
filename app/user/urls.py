'''
URL mappings for the user API
'''
from django.urls import path

from app.user import views

app_names = 'user'

urlpatterns = [
    path('create/', views.CreateUserViews.as_view(), name='create'),

]
