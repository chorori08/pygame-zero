import pgzrun
from random import randint          # 랜덤 한 수를 가져오기 위해서 임포트

miss=0

apple=Actor("apple")

# 화면을 그리는 부분
def draw():
    screen.clear()
    apple.draw()
    if(miss==1):
        screen.fill("black")
        screen.draw.text("You missed!",center=(400,300),fontsize=100)

def place_apple():
    apple.x=randint(10,800)         # 10부터 800사이에 랜덤한 정수를 가져오는 것
    apple.y=randint(10,600)         # 10부터 600사이에 랜덤한 정수를 가져오는 것

# 마우스 클릭 이벤트 함수
def on_mouse_down(pos):
    global miss                     # 밖에 있는 변수를 함수 안으로 넣을때 쓰는 것

    if(miss==1):                    # 실행되는 순서가 매우 중요함, miss를 먼저 변경하고 게임을 종료하기 위해
        quit()

    if apple.collidepoint(pos):     # apple을 클릭할떄
        print("Good shot")
        place_apple()
    else:
        print("You missed!")
        miss=1
        # quit()                    # 실행을 끝낸다




place_apple()                       # 함수호출은 함수이름 그대로



pgzrun.go()

# 실패 하였을때 You missed! 라는 글씨가 화면에 크게 나타나기
# 사과의 위치가 1초에 한번씩 바뀌고,1초 안에 클릭 못할 시 실패