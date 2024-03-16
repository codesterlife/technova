from django.contrib import admin

# Register your models here.
from . models import *

admin.site.register(Quiz)

# level 1 -> task 1 -> mcq -> models
class ChoiceAdmin(admin.StackedInline):
    model = MCQChoice

class MCQQuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceAdmin]

admin.site.register(MCQQuestion, MCQQuestionAdmin)
admin.site.register(MCQChoice)

# level 1 -> task 2 -> qna -> models
class QNAAnswerAdmin(admin.StackedInline):
    model = QNAAnswer

class QNAQuestionAdmin(admin.ModelAdmin):
    inlines = [QNAAnswerAdmin]

admin.site.register(QNAQuestion, QNAQuestionAdmin)
admin.site.register(QNAAnswer)