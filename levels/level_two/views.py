from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from levels.level_one.models import Quiz
from .forms import Hexahue
from accounts.models import Score, VisitedTasks

hexahue_cipher = "TEVA{N07hin9 41iv3 c4n b3 c41cu14t3d.}"
audio_decode_cipher = "TEVA{fearisthemindkiller}"
img_decode_answer = "TEVA{stenography}"

# Create your views here.
@login_required(login_url='../../../accounts/login')
def level_two_dashboard(request): 
    return render(request, 'level_two_dashboard.html')

# level 2 -> task 1 -> Picture to code
    
@login_required(login_url='../../../accounts/login')
def picture_to_code_detail_view(request):
    user_visited = VisitedTasks.objects.get(user = request.user)
    if user_visited.visited_level2_task1 != True:
        return render(request, 'picture-to-code/picture-to-code.html')
    else:
        return render(request, '../templates/already_played.html')

@login_required(login_url='../../../accounts/login')
def online_ide_view(request):
    return render(request, 'picture-to-code/online-ide.html')

@login_required(login_url='../../../accounts/login')
def picture_to_code_submit_view(request):
    if request.method == "POST":
        score = 50 # change the value accordingly
        user = Score.objects.get(user = request.user)
        user.score += score
        user.save()

        user_visited = VisitedTasks.objects.get(user = request.user)
        user_visited.visited_level2_task1 = True
        user_visited.save()

        context = {'score': score, 'user_score': user.score}
        return render(request, 'picture-to-code/picture-to-code-result.html', context)
    
# level 2 -> task 2 -> audio decode

@login_required(login_url='../../../accounts/login')
def audio_decode_detail_view(request):
    user_visited = VisitedTasks.objects.get(user = request.user)
    if user_visited.visited_level2_task2 != True:
        form = Hexahue()
        context = {'form': form, 'cipher': audio_decode_cipher}
        return render(request, 'audio-decode/audio_decode.html', context)
    else:
        return render(request, '../templates/already_played.html')

@login_required(login_url='../../../accounts/login')
def audio_decode_submit_view(request):
    correct_answer = audio_decode_cipher
    if request.method == 'POST':
        form = Hexahue(request.POST) # using the hexahue form because both games have a similar interface.
        score = 0
        if form.is_valid():
            answer = form.cleaned_data['answer']
            if answer.lower() == correct_answer.lower():
                score += 50 # Change the value accordingly
                
        user = Score.objects.get(user = request.user)
        user.score += score
        user.save()

        user_visited = VisitedTasks.objects.get(user = request.user)
        user_visited.visited_level2_task2 = True
        user_visited.save()

        context = {'score': score, 'user_score': user.score}
        return render(request, 'audio-decode/audio_decode_result.html', context)
            
    return redirect("levels:level-two:audio_decode_detail")

# level 2 -> task 3 -> hexahue decoding

@login_required(login_url='../../../accounts/login')
def hexahue_detail_view(request):
    user_visited = VisitedTasks.objects.get(user = request.user)
    if user_visited.visited_level2_task3 != True:
        form = Hexahue()
        context = {'form': form, 'cipher': hexahue_cipher}
        return render(request, 'hexahue/hexahue.html', context)
    else:
        return render(request, '../templates/already_played.html')

@login_required(login_url='../../../accounts/login')
def hexahue_submit_view(request):
    correct_answer = hexahue_cipher
    if request.method == 'POST':
        form = Hexahue(request.POST)
        score = 0
        if form.is_valid():
            answer = form.cleaned_data['answer']
            if answer.lower() == correct_answer.lower():
                score += 50 # Change the value accordingly
                
        user = Score.objects.get(user = request.user)
        user.score += score
        user.save()

        user_visited = VisitedTasks.objects.get(user = request.user)
        user_visited.visited_level2_task3 = True
        user_visited.save()

        context = {'score': score, 'user_score': user.score}
        return render(request, 'hexahue/hexahue_result.html', context)
            
    return redirect("levels:level-two:hexahue_detail")

# level 2 -> task 4 -> Image decode.

@login_required(login_url='../../../accounts/login')
def img_decode_detail_view(request):
    user_visited = VisitedTasks.objects.get(user = request.user)
    if user_visited.visited_level2_task4 != True:
        form = Hexahue()
        context = {'form': form, 'answer': img_decode_answer}
        return render(request, 'img-decode/img_decode.html', context)
    else:
        return render(request, '../templates/already_played.html')


@login_required(login_url='../../../accounts/login')
def img_decode_submit_view(request):
    correct_answer = img_decode_answer
    if request.method == 'POST':
        form = Hexahue(request.POST) # using the hexahue form because both games have a similar interface.
        score = 0
        if form.is_valid():
            answer = form.cleaned_data['answer']
            if answer.lower() == correct_answer.lower():
                score += 50 # Change the value accordingly
                
        user = Score.objects.get(user = request.user)
        user.score += score
        user.save()

        user_visited = VisitedTasks.objects.get(user = request.user)
        user_visited.visited_level2_task4 = True
        user_visited.save()

        context = {'score': score, 'user_score': user.score}
        return render(request, 'img-decode/img_decode_result.html', context)
            
    return redirect("levels:level-two:img_decode_detail")
