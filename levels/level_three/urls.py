from django.urls import path
from . import views

app_name = 'level-three'

urlpatterns = [
    path('', views.level_three_dashboard, name='level-three-dashboard'),
    path('task/', views.location_guesser_detail_view, name='location_guesser_detail'),
    path('task/submit/', views.location_guesser_submit_view, name='location_guesser_submit'),
]