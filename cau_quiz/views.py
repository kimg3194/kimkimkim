from django.shortcuts import render, redirect
from .models import Quiz
from .models import Player
#from django.utils import timezone
import time
#from .form import Player

# Create your views here.

def home(request):
    return render(request, 'home.html')

def index(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    player = Player.objects.latest('id')
    return render(request,'index.html',{'quiz' : quiz,'player' : player})

def endgame(request, player_id):
    return render(request,'endgame.html')

def createPlayer(request):
    player = Player()
    player.name = request.GET['playername']
    #player.pub_date_1 = timezone.datetime.now()
    player.save()
    return redirect('/')

# def player(request):
#    if request.method == 'POST'
#        form = Player(request.POST)
#        if form.is_valid():
#            post = form.save(commit=False)
#            post.save()
#            return redirect('home')
#     else:
#         form = Player()
#         return render(request, '.html', {})

# def move(request):
#     return redirect('/')

def answer(request, quiz_id):
    player = Player.objects.latest('id')
    player.setMedal()
    print(player.medal)
    if quiz_id ==13:
        return render(request,'endgame.html',{'player' : player})

    quiz = Quiz.objects.get(id=quiz_id)
    if request.POST['answer'] == quiz.answer:
        print("정답입니다.")
        quiz = Quiz.objects.get(id=quiz_id+1)
        player.increase()
        player.status = "true"
    else:
        print("오답입니다.")
        quiz = Quiz.objects.get(id=quiz_id+1)
        print(quiz)
        player.status = "false"
        print(player.medal)

    if quiz.id == 1:
        player.position = "marker102"
    elif quiz.id ==2:
        player.position = "marker105"
    elif quiz.id ==3:
        player.position = "marker106"
    elif quiz.id ==4:
        player.position = "marker204"
    elif quiz.id ==5:
        player.position = "markerH"
    elif quiz.id ==6:
        player.position = "marker207"
    # elif quiz_id ==8:
    #     player.position = "marker208"
    elif quiz_id ==7:
        player.position = "marker308"
    elif quiz_id ==8:
        player.position = "marker309"
    elif quiz_id ==9:
        player.position = "marker310"
    elif quiz_id ==10:
        player.position = "marker303"
    elif quiz_id ==11:
        player.position = "marker305"
    elif quiz_id ==12:
        player.position = "markerBackYard"
    else:
        player.position = "marker208"
    return render(request,'index.html',{'quiz' : quiz, 'player' : player})