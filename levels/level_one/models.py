from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length=255, default="default-title")
    description = models.TextField(default="default-desc")

    def __str__(self):
        return self.title
    
# level 1 -> task 1 -> mcq -> models

class MCQQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=255)
    img = models.ImageField(upload_to='img_quiz', blank=True, null=True, height_field="img_height", width_field="img_width")
    img_height = models.IntegerField(blank=True, null=True)
    img_width = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.question_text

class MCQChoice(models.Model):
    question = models.ForeignKey(MCQQuestion, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return "{0} --> {1}".format(self.question.question_text, self.choice_text)
    
# level 1 -> task 2 -> qna -> models
    
class QNAQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    qna_question = models.TextField()
    img = models.ImageField(upload_to='img_quiz', blank=True, null=True, height_field="img_height", width_field="img_width")
    img_height = models.IntegerField(blank=True, null=True)
    img_width = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.qna_question
    
class QNAAnswer(models.Model):
    question = models.ForeignKey(QNAQuestion, on_delete=models.CASCADE)
    qna_answer = models.CharField(max_length=255)

    def __str__(self):
        return self.qna_answer