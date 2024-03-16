from django.urls import path, include
from . import views

app_name = "level-one"

urlpatterns = [
    path('', views.level_one_dashboard, name='level-one-dashboard'),
    path('task-<int:pk>/mcq', views.mcq_detail_view, name='quiz_detail'),
    path('task-<int:pk>/mcq/submit/', views.mcq_submit_view, name='quiz_submit'),
    path('task-<int:pk>/qna', views.qna_detail_view, name='qna_detail'),
    path('task-<int:pk>/qna/submit/', views.qna_submit_view, name='qna_submit'),
    path('task-3/sudoku', views.sudoku_detail_view, name='sudoku_detail'),
    path('task-3/sudoku/submit/', views.sudoku_submit_view, name='sudoku_submit'),
    path('task-4/puzzle', views.puzzle_detail_view, name='puzzle_detail'),
    path('task-4/puzzle/submit/', views.puzzle_submit_view, name='puzzle_submit'),
    path('task-5/crossword', views.crossword_detail_view, name='crossword_detail'),
    path('task-5/crossword/submit/', views.crossword_submit_view, name='crossword_submit'),
]