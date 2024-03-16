from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='site-home'),
    path('home/', views.homepage, name='technova-home'),
    path('accounts/', include('accounts.urls'), name="accounts"),
    path('profile/', views.profile, name='user-profile'),
    path('dashboard/', views.dashboard, name="technova-dashboard"),
    path('levels/', include('levels.urls'), name='levels'),
    path('scoreboard/', views.scoreboard, name="technova-scoreboard")
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

