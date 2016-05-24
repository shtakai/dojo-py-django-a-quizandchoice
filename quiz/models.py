from django.db import models

# Create your models here.
class Quiz(models.Model):
    created_at    = models.DateField(auto_now=True)
    updated_at    = models.DateField(auto_now=True)
    question_text = models.CharField(max_length=255)
    pud_date      = models.DateField(auto_now=True)

    class Meta:
        db_table = 'quizzes'


class Choice(models.Model):
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)
    quiz       = models.ForeignKey(Quiz)

    class Meta:
        db_table = 'choices'

