from django.db import models
from django.utils import timezone
import time

# Create your models here.
class Quiz(models.Model):
    quiz = models.TextField()
    answer = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default="default")

    def __str__(self):
        return self.quiz

class Player(models.Model):
    name = models.CharField(max_length=10)
    score = models.IntegerField(default = 0)
    medal = models.CharField(max_length=10, default="hi")
    position = models.CharField(max_length=10, default="marker102")
    image = models.ImageField(upload_to='images/', default="chicken.PNG")

    pub_date_1 = models.DateTimeField('date published', default=timezone.datetime.now())
    pub_date_2 = models.DateTimeField('date published', default=timezone.datetime.now())
    def __str__(self):
        return self.name

    def increase(self):
        self.score +=1
        self.save()

    def setMedal(self):
        if(self.score>=0 and self.score<3):
            self.medal = "샌액희"
        elif(self.score>=3 and self.score<6):
            self.medal = "고려청자"
        elif(self.score>=6 and self.score<9):
            self.medal = "고인돌"
        elif(self.score>=9 and self.score<12):
            self.medal = "시조새"
        elif(self.score>=12):
            self.medal = "암모나이트"
            self.save()

    # def timeCalc(self):
    #     self.result = (pub_date_2-pub_date_1).seconds
    #     self.save()

