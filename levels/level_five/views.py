from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from accounts.models import Score, VisitedTasks
from levels.level_two.forms import Hexahue

clue1_answer = "TEVA{891.8133G1 TIM}"
clue2_answer = "TEVA{unfurled}"
clue3_answer = "TEVA{sycamore}"
clue4_answer = "TEVA{}"

# Create your views here.
def level_five_dashboard(request):
    user = Score.objects.get(user = request.user)
    required_score = 200 # change this value as per requirement.
    if (user.score >= required_score):  
        return render(request, 'level_five_dashboard.html')
    elif (user.score < required_score):
        return render(request, '../templates/score_not_enough.html')

def clue_toggle(request, context):
    user_visited = VisitedTasks.objects.get(user = request.user)
    if user_visited.visited_level5_task_clue1 == True:
        context['clue1_complete'] = True
    if user_visited.visited_level5_task_clue2 == True:
        context['clue2_complete'] = True
    if user_visited.visited_level5_task_clue3 == True:
        context['clue3_complete'] = True
    if user_visited.visited_level5_task_clue4 == True:
        context['clue4_complete'] = True

    return context

@login_required(login_url='../../../accounts/login')
def treasure_hunt_detail_view(request):
    context = {}
    clue_toggle(request, context)

    return render(request, 'treasure-hunt/treasure_hunt.html', context)
    
@login_required(login_url='../../../accounts/login')
def clue_one(request):
    user_visited = VisitedTasks.objects.get(user = request.user)
    if user_visited.visited_level5_task_clue1 != True:
        form = Hexahue()
        context = {'form': form, 'answer': clue1_answer}
        return render(request, 'treasure-hunt/start.html', context)
    else:
        return render(request, '../templates/already_played.html')

@login_required(login_url='../../../accounts/login')
def clue_two(request):
    user_visited = VisitedTasks.objects.get(user = request.user)
    if user_visited.visited_level5_task_clue2 != True:
        user_visited = VisitedTasks.objects.get(user = request.user)
        user_visited.visited_level5_task_clue1 = True
        user_visited.save()

        form = Hexahue()
        context = {'form': form, 'answer': clue2_answer}
        clue_toggle(request, context)
        return render(request, 'treasure-hunt/clue-2.html', context)
    else:
        return render(request, '../templates/already_played.html')

@login_required(login_url='../../../accounts/login')
def clue_three(request):
    user_visited = VisitedTasks.objects.get(user = request.user)
    if user_visited.visited_level5_task_clue3 != True:
        user_visited = VisitedTasks.objects.get(user = request.user)
        user_visited.visited_level5_task_clue2 = True
        user_visited.save()

        form = Hexahue()
        context = {'form': form, 'answer': clue3_answer}
        clue_toggle(request, context)
        return render(request, 'treasure-hunt/clue-3.html', context)
    else:
        return render(request, '../templates/already_played.html')

@login_required(login_url='../../../accounts/login')
def clue_four(request):
    user_visited = VisitedTasks.objects.get(user = request.user)
    if user_visited.visited_level5_task_clue4 != True:
        user_visited.visited_level5_task_clue3 = True
        user_visited.save()

        form = Hexahue()
        context = {'form': form, 'answer': clue4_answer}
        clue_toggle(request, context)
        return render(request, 'treasure-hunt/finish.html', context)
    else:
        return redirect('levels:levels-dashboard')

@login_required(login_url='../../../accounts/login')
def wiki_start(request):
    return render(request, 'treasure-hunt/wiki.html')

@login_required(login_url='../../../accounts/login')
def clue_four_submit_view(request):
    if request.method == "POST":
        score = 200 # change the value accordingly
        user = Score.objects.get(user = request.user)
        user.score += score
        user.save()

        user_visited = VisitedTasks.objects.get(user = request.user)
        user_visited.visited_level5_task_clue4 = True
        user_visited.visited_level5_task = True
        user_visited.save()

        context = {'score': score, 'user_score': user.score}
        return render(request, 'treasure-hunt/treasure_hunt_result.html', context)