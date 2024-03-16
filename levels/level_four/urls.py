from django.urls import path
from . import views

app_name = 'level-four'

urlpatterns = [
    path('', views.level_four_dashboard, name='level-four-dashboard'),
    path('task1/', views.spectral_analyzer_detail_view, name='spectral_analyzer_detail'),
    path('task1/submit/', views.spectral_analyzer_submit_view, name='spectral_analyzer_submit'),
    path('task2/', views.blind_coding_detail_view, name='blind_coding_detail'),
    path('task2/ide/', views.online_ide_view, name='online_ide'),
    path('task2/submit/', views.blind_coding_submit_view, name='blind_coding_submit')
]