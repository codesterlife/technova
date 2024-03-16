from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from levels.level_two.forms import Hexahue
from accounts.models import Score, VisitedTasks

spectral_analyzer_cipher = "TEVA{The_life_of_Pablo}"

# Create your views here.
def level_four_dashboard(request):
    user = Score.objects.get(user = request.user)
    required_score = 200 # change this value as per requirement.
    if (user.score >= required_score):  
        return render(request, 'level_four_dashboard.html')
    elif (user.score < required_score):
        return render(request, '../templates/score_not_enough.html')

# level 4 -> task 1 -> Spectral Analyzer

@login_required(login_url='../../../accounts/login')
def spectral_analyzer_detail_view(request):
    user_visited = VisitedTasks.objects.get(user = request.user)
    if user_visited.visited_level4_task1 != True:
        form = Hexahue()
        context = {'form': form, 'cipher': spectral_analyzer_cipher}
        return render(request, 'spectral-analysis/spectral_analyzer.html', context)
    else:
        return render(request, '../templates/already_played.html')

@login_required(login_url='../../../accounts/login')
def spectral_analyzer_submit_view(request):
    correct_answer = spectral_analyzer_cipher
    if request.method == 'POST':
        form = Hexahue(request.POST) # using the hexahue form because both games have a similar interface.
        score = 0
        if form.is_valid():
            answer = form.cleaned_data['answer']
            if answer.lower() == correct_answer.lower():
                score += 100 # Change the value accordingly
                
        user = Score.objects.get(user = request.user)
        user.score += score
        user.save()

        user_visited = VisitedTasks.objects.get(user = request.user)
        user_visited.visited_level4_task1 = True
        user_visited.save()

        context = {'score': score, 'user_score': user.score}
        return render(request, 'spectral-analysis/spectral_analyzer_result.html', context)
            
    return redirect("levels:level-four:spectral_analyzer_detail")

# level 4 -> task2 -> Blind Coding

@login_required(login_url='../../../accounts/login')
def blind_coding_detail_view(request):
    user_visited = VisitedTasks.objects.get(user = request.user)
    if user_visited.visited_level4_task2 != True:
        return render(request, 'blind-coding/blind-coding.html')
    else:
        return render(request, '../templates/already_played.html')

@login_required(login_url='../../../accounts/login')
def online_ide_view(request):
    return render(request, 'blind-coding/online-ide.html')

@login_required(login_url='../../../accounts/login')
def blind_coding_submit_view(request):
    if request.method == "POST":
        score = 100 # change the value accordingly
        user = Score.objects.get(user = request.user)
        user.score += score
        user.save()

        user_visited = VisitedTasks.objects.get(user = request.user)
        user_visited.visited_level4_task2 = True
        user_visited.save()

        context = {'score': score, 'user_score': user.score}
        return render(request, 'blind-coding/blind-coding-result.html', context)