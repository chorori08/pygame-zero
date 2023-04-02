import pgzrun
from random import randint

WIDTH=400
HEIGHT=400

score=0
game_over=False

fox=Actor("fox")
fox.pos=100,100
coin=Actor("coin")
coin.pos=200,200
hedgehog=Actor("hedgehog")
hedgehog.pos=150,150

def draw():

    screen.fill("green")                       # 배경색깔 초록색으로 변경

    fox.draw()                                 # 화면에 여우 띄우기
    coin.draw()
    hedgehog.draw()

    screen.draw.text("Score:"+str(score),color="black",topleft=(10,10))

    if game_over:                              # 게임 끝났을때 나오는 화면
        screen.fill("pink")
        screen.draw.text("Final Score:"+str(score),topleft=(10,10),fontsize=60)

        if score>=50:
            screen.draw.text("Success",center=(200,200),fontsize=100)
        else:
            screen.draw.text("Fail",center=(200,200),fontsize=100)


def place_coin():
    coin.x=randint(20,(WIDTH-20))
    coin.y=randint(20,(HEIGHT-20))


def place_hedgehog():
    hedgehog.x=randint(20,(WIDTH-20))
    hedgehog.y=randint(20,(HEIGHT-20))


def time_up():
    global game_over
    game_over=True


def update():
    global score 

    if keyboard.left:
        fox.x=fox.x-2
    elif keyboard.right:
        fox.x=fox.x+2

    if keyboard.up:
        fox.y=fox.y-2
    elif keyboard.down:
        fox.y=fox.y+2

    coin_collected=fox.colliderect(coin)       # 여우가 코인과 겹첬을때의 내용
    hedgehog_collected=fox.colliderect(hedgehog)

    if coin_collected:
        score=score+10                         # score+=10으로 해도 됨
        place_coin()
        place_hedgehog()
    elif hedgehog_collected:
        score=score-10                        
        place_hedgehog()
        place_coin()

clock.schedule(time_up,8.0)                    # 7초뒤 예약
place_coin()                                   # 위치를 랜덤으로 바뀌게 하는 함수
place_hedgehog()

pgzrun.go()


# 랜덤하게 위치한 장애물 만들기(장애물 닿을시 -10점)
# 점수가 50점 이상이면 "Success",미만이면 "Fail" 표시 뜨게 하기