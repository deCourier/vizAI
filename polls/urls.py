from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('index/', views.IndexView.as_view(), name='index'),
    path('inner-page/', views.InnerView.as_view(), name='inner-page'),
    path('cancer/', views.CancerView.as_view(), name='cancer'),
    path('alcohol/', views.AlcoholView.as_view(), name='alcohol'),
    path('housing/', views.HousingView.as_view(), name='housing'),
    path('nba/', views.NBAView.as_view(), name='nba'),
    path('diabetes/', views.DiabetesView.as_view(), name='diabetes'),
    path('unemployment/', views.UnemploymentView.as_view(), name='unemployment'),
] 
