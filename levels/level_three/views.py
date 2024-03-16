from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from accounts.models import Score, VisitedTasks

# Create your views here.

@login_required(login_url='../../../accounts/login')
def level_three_dashboard(request):
    user = Score.objects.get(user = request.user)
    required_score = 200 # change this value as per requirement.
    if (user.score >= required_score):  
        return render(request, 'level_three_dashboard.html')
    elif (user.score < required_score):
        return render(request, '../templates/score_not_enough.html')
    
@login_required(login_url='../../../accounts/login')
def location_guesser_detail_view(request):
    user_visited = VisitedTasks.objects.get(user = request.user)
    if user_visited.visited_level3_task != True:
        return render(request, "location-guesser/location_guesser.html")
    else:
        return render(request, '../templates/already_played.html')

@login_required(login_url='../../../accounts/login')
def location_guesser_submit_view(request):
    if request.method == 'POST':
        score = 100 # change the value accordingly
        user = Score.objects.get(user = request.user)
        user.score += score
        user.save()

        user_visited = VisitedTasks.objects.get(user = request.user)
        user_visited.visited_level3_task = True
        user_visited.save()
        context = {'score': score, 'user_score': user.score}

    return render(request, "location-guesser/location_guesser_result.html", context)