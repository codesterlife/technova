from django.urls import path, include
from . import views

app_name = 'levels'

urlpatterns = [
    path('', views.levels_dashboard, name='levels-dashboard'),
    path('level1/', include('levels.level_one.urls')), 
    path('level2/', include('levels.level_two.urls')),
    path('level3/', include('levels.level_three.urls')),
    path('level4/', include('levels.level_four.urls')),
    path('level5/', include('levels.level_five.urls')),
]