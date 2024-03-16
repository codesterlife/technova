from django.urls import path
from . import views

app_name = 'level-five'

urlpatterns = [
    path('', views.level_five_dashboard, name='level-five-dashboard'),
    path('task/', views.treasure_hunt_detail_view, name='treasure_hunt_detail'),
    path('task/clue1', views.clue_one, name='clue_one'),
    path('task/clue2', views.clue_two, name='clue_two'),
    path('task/clue3', views.clue_three, name='clue_three'),
    path('task/clue4', views.clue_four, name='clue_four'),
    path('task/clue4/start', views.wiki_start, name='clue_four_wiki'),
    path('task/clue4/submit/', views.clue_four_submit_view, name='clue_four_submit'),
]