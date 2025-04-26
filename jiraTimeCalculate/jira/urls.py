from django.urls import path
from . import views

urlpatterns = [
    path('jira/', views.jira_page, name='jira_page'),
]