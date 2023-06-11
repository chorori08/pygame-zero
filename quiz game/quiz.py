import pgzrun

WIDTH=1280
HEIGHT=720

main_box=Rect(0,0,820,240)
timer_box=Rect(0,0,240,240)
answer_box1=Rect(0,0,495,165)
answer_box2=Rect(0,0,495,165)
answer_box3=Rect(0,0,495,165)
answer_box4=Rect(0,0,495,165)

main_box.move_ip(50,40)
timer_box.move_ip(990,40)
answer_box1.move_ip(50,358)
answer_box2.move_ip(735,358)
answer_box3.move_ip(50,538)
answer_box4.move_ip(735,538)
answer_boxes=[answer_box1,answer_box2,answer_box3,answer_box4]

score=0
time_left=7

q1=["What is the capital of Republic of Suriname?","Jerusalem","Ankara","Helsinki","Paramaribo",4]
q2=["Who is the presidant of Republic of Suriname?","Ukhnaagiin Khurelsukh","Mark Rutte","Chan Santokhi","Yitzhak Herzog",3]
q3=["How many Ballon d'Or does Lionel Messi have?","4","7","6","9",2]
q4=["Who scored the most goals in the England Premier League?","Harry Kane","Wayne Rooney","Heungmin Son","Alan Shearer",4]
q5=["Who scored the most goals in the 2022 Qatar World Cup?","Harry Kane","Lional Messi","Kylian Mbappe","Cristiano Ronaldo",3]
questions=[q1,q2,q3,q4,q5]
question=questions.pop(0)

def draw():
    screen.fill("black")
    screen.draw.filled_rect(main_box,"deep pink")
    screen.draw.filled_rect(timer_box,"deep pink")

    for box in answer_boxes:
        screen.draw.filled_rect(box,"deep pink")

    screen.draw.textbox(str(time_left),timer_box,color=("black"))
    screen.draw.textbox(question[0],main_box,color=("black"))

    index=1
    for box in answer_boxes:
        screen.draw.textbox(question[index],box,color=("black"))
        index+=1

def game_over():
    global question,time_left
    message="game over.You got %s questions correct"%str(score)
    question=[message,"_","_","_","_"]
    time_left=0

def correct_answer():
    global question,score,time_left

    score+=1
    if questions:
        question=questions.pop(0)
        time_left=7
    else:
        game_over()    

def on_mouse_down(pos):
    index=1
    for box in answer_boxes:
        if box.collidepoint(pos):
            print("Clicked on answer"+str(index))
            if index==question[5]:
                correct_answer()
            else:
                game_over()
        index+=1

def update_time_left():
    global time_left 

    if time_left:
        time_left-=1
    else:
        game_over()

def on_key_up(key):
    global score
    if key==keys.SPACE:
        correct_answer()
        score-=1

clock.schedule_interval(update_time_left,1.0)

pgzrun.go()