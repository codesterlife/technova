from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from accounts.models import VisitedTasks

# Create your views here.

def check_level_completion(request, context, level):
    user_visited = VisitedTasks.objects.get(user = request.user)
    if (level == "level1"):
        if user_visited.visited_level1_task1 == True and user_visited.visited_level1_task2 == True and user_visited.visited_level1_task3 == True and user_visited.visited_level1_task4 == True and user_visited.visited_level1_task5 == True:
            context['level1_complete'] = True
        return context
    
    if (level == "level2"):
        if user_visited.visited_level2_task1 == True and user_visited.visited_level2_task2 == True and user_visited.visited_level2_task3 == True and user_visited.visited_level2_task4 == True:
            context['level2_complete'] = True
        return context
    
    if (level == "level3"):
        if user_visited.visited_level3_task == True:
            context['level3_complete'] = True
        return context

    if (level == "level4"):
        if user_visited.visited_level4_task1 == True and user_visited.visited_level4_task2 == True:
            context['level4_complete'] = True
        return context
    
    if (level == "level5"):
        if user_visited.visited_level5_task == True and user_visited.visited_level5_task_clue1 == True and user_visited.visited_level5_task_clue2 == True and user_visited.visited_level5_task_clue3 == True and user_visited.visited_level5_task_clue4 == True:
            context['level5_complete'] = True
        return context

    
@login_required(login_url=('../../accounts/login'))
def levels_dashboard(request):
    context = {}
    check_level_completion(request, context, level="level1")
    check_level_completion(request, context, level="level2")
    check_level_completion(request, context, level="level3")
    check_level_completion(request, context, level="level4")
    check_level_completion(request, context, level="level5")
    
    if context == {'level1_complete': True, 'level2_complete': True, 'level3_complete': True, 'level4_complete': True, 'level5_complete': True}:
        return render(request, 'jackpot.html')
    else:
        return render(request, 'levels_dashboard.html', context)

