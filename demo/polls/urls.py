from django.urls import path # importing the path module 
from . import views # importing the views from the current directory

app_name = 'polls' #namespace for this specific app
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]