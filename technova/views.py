from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import Score

def index(request):
    return render(request, "index.html")

@login_required(login_url="/accounts/login")
def homepage(request):
    #return HttpResponse("Home")
    return render(request, "homepage.html")

@login_required(login_url="/accounts/login")
def dashboard(request):
    #return HttpResponse("dashboard")
    return render(request, 'dashboard.html')

@login_required(login_url="/accounts/login")
def profile(request):
    #return HttpResponse("Profile")
    return render(request, 'profile.html')

@login_required(login_url="/accounts/login")
def scoreboard(request):
    scores = Score.objects.all().order_by('-score')
    return render(request, 'scoreboard.html', {'scores' : scores})