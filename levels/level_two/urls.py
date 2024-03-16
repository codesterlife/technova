from django.urls import path
from . import views

app_name = 'level-two'

urlpatterns = [
    path('', views.level_two_dashboard, name='level-two-dashboard'),
    path('task1/', views.picture_to_code_detail_view, name='picture_to_code_detail'),
    path('task1/ide/', views.online_ide_view, name='online_ide'),
    path('task1/submit/', views.picture_to_code_submit_view, name='picture_to_code_submit'),
    path('task2/', views.audio_decode_detail_view, name='audio_decode_detail'),
    path('task2/submit/', views.audio_decode_submit_view, name='audio_decode_submit'),
    path('task3/', views.hexahue_detail_view, name='hexahue_detail'),
    path('task3/submit/', views.hexahue_submit_view, name='hexahue_submit'),
    path('task-4/img-decode', views.img_decode_detail_view, name='img_decode_detail'),
    path('task-4/img-decode/submit/', views.img_decode_submit_view, name='img_decode_submit'),
]