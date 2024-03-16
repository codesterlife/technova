from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from levels.level_one.models import Quiz
from accounts.models import Score, VisitedTasks

# Create your views here.
@login_required(login_url='../../../accounts/login')
def level_one_dashboard(request):
    context = {'quiz' : [i for i in Quiz.objects.all()]}
    return render(request, 'level_one_dashboard.html', context)

@login_required(login_url='../../../accounts/login')
def mcq_detail_view(request, pk):
    user_visited = VisitedTasks.objects.get(user = request.user)
    if user_visited.visited_level1_task1 != True:
        quiz = Quiz.objects.get(pk=pk)
        mcq_questions = quiz.mcqquestion_set.all().order_by('?')
        context = {'quiz': quiz, 'mcq_questions': mcq_questions}
        return render(request, 'mcq/quiz.html', context)
    else:
        return render(request, '../templates/already_played.html')

@login_required(login_url='../../../accounts/login')
def mcq_submit_view(request, pk):
    if request.method == 'POST':
        quiz = Quiz.objects.get(pk=pk)
        mcq_questions = quiz.mcqquestion_set.all()

        # Initialize score and correct count
        score = 0
        count = 0
        max_score = len(mcq_questions) * 2

        # Loop through questions and check submitted answers
        for question in mcq_questions:
            submitted_choice_id = request.POST.get(f'question_{question.id}')
            correct_choice_id = question.mcqchoice_set.filter(is_correct=True).first().id

            # Check if the submitted choice is correct
            if submitted_choice_id == str(correct_choice_id):
                score += 2 # change this value accordingly. # 15 x 2 = 30
                count += 1

        user = Score.objects.get(user = request.user)
        user.score += score
        user.save()
        user_visited = VisitedTasks.objects.get(user = request.user)
        user_visited.visited_level1_task1 = True
        user_visited.save()

        context = {'quiz': quiz, 'q_count': len(mcq_questions), 'score': score, 'count':count, 'user_score': user.score, 'max_score': max_score}

        # Assuming a simple scoring system (2 point per correct answer)
        # You might want to customize this based on your requirements

        return render(request, 'mcq/quiz_result.html', context)

    # Redirect to the quiz page if the request method is not POST
    return redirect("levels:level-one:quiz_detail")

# level 1 -> task 2 -> Question Answer game.

@login_required(login_url='../../../accounts/login')
def qna_detail_view(request, pk):
    user_visited = VisitedTasks.objects.get(user = request.user)
    if user_visited.visited_level1_task2 != True:
        quiz = Quiz.objects.get(pk=pk)
        qna_questions = quiz.qnaquestion_set.all().order_by('?')
        context = {'quiz': quiz, 'qna_questions': qna_questions}
        return render(request, 'qna/qna.html', context)
    else:
        return render(request, '../templates/already_played.html')
        

@login_required(login_url='../../../accounts/login')
def qna_submit_view(request, pk):
    if request.method == 'POST':
        quiz = Quiz.objects.get(pk=pk)
        qna_questions = quiz.qnaquestion_set.all()

        # Initialize score and correct count
        score = 0
        count = 0
        max_score = len(qna_questions) * 2

        # Loop through questions and check submitted answers
        for question in qna_questions:
            submitted_answer = request.POST.get(f'question_{question.id}')
            correct_answer = question.qnaanswer_set.all().values()[0]['qna_answer']

            # Check if the submitted answer is correct
            if submitted_answer.lower() == correct_answer.lower():
                score += 2 # Change the value here accordingly. # 15 x 2 = 30
                count += 1

        user = Score.objects.get(user = request.user)
        user.score += score
        user.save()
        user_visited = VisitedTasks.objects.get(user = request.user)
        user_visited.visited_level1_task2 = True
        user_visited.save()

        context = {'quiz': quiz, 'q_count': len(qna_questions), 'score': score, 'count': count, 'user_score': user.score, 'max_score': max_score}

        return render(request, 'qna/qna_result.html', context)

    # Redirect to the qna page if the request method is not POST
    return redirect("levels:level-one:qna_detail")



# level 1 -> task 3 -> Sudoku

@login_required(login_url='../../../accounts/login')
def sudoku_detail_view(request):
    user_visited = VisitedTasks.objects.get(user = request.user)
    if user_visited.visited_level1_task3 != True:
        return render(request, 'sudoku/sudoku.html', )
    else:
        return render(request, '../templates/already_played.html')
    
@login_required(login_url='../../../accounts/login')
def sudoku_submit_view(request):
    if request.method == 'POST': 
        user_visited = VisitedTasks.objects.get(user = request.user)
        user_visited.visited_level1_task3 = True
        user_visited.save()

        user = Score.objects.get(user = request.user)
        user.score += 20 # Change the value here accordingly. 
        user.save()

        context = {'user_score': user.score}
        return render(request, 'sudoku/sudoku_result.html', context)
    
    # Redirect to the sudoku_detail page if the request method is not POST
    return redirect("levels:level-one:sudoku_detail")

# level 1 -> task 4 -> Jigsaw puzzle

@login_required(login_url='../../../accounts/login')
def puzzle_detail_view(request):
    user_visited = VisitedTasks.objects.get(user = request.user)
    if user_visited.visited_level1_task4 != True:
        return render(request, 'puzzle/puzzle.html')
    else:
        return render(request, '../templates/already_played.html')
    
@login_required(login_url='../../../accounts/login')
def puzzle_submit_view(request):
    if request.method == 'POST': 
        user_visited = VisitedTasks.objects.get(user = request.user)
        user_visited.visited_level1_task4 = True
        user_visited.save()

        user = Score.objects.get(user = request.user)
        user.score += 20 # Change the value here accordingly. 
        user.save()

        context = {'user_score': user.score}
        return render(request, 'puzzle/puzzle_result.html', context)
    
    # Redirect to the puzzle detail page if the request method is not POST
    return redirect("levels:level-one:puzzle_detail")

# level 1 -> task 5 -> Crossword

@login_required(login_url='../../../accounts/login')
def crossword_detail_view(request):
    user_visited = VisitedTasks.objects.get(user = request.user)
    if user_visited.visited_level1_task5 != True:
        return render(request, 'crossword/crossword.html', )
    else:
        return render(request, '../templates/already_played.html')

@login_required(login_url='../../../accounts/login')
def crossword_submit_view(request):
    if request.method == 'POST': 
        user_visited = VisitedTasks.objects.get(user = request.user)
        user_visited.visited_level1_task5 = True
        user_visited.save()

        user = Score.objects.get(user = request.user)
        user.score += 20 # Change the value here accordingly. 
        user.save()

        context = {'user_score': user.score}
        return render(request, 'crossword/crossword_result.html', context)

    # Redirect to the crossword detail page if the request method is not POST
    return redirect("levels:level-one:crossword_detail")