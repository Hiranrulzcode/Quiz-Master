import pgzrun

WIDTH=870
HEIGHT=650
TITLE="Quiz Master"

question_box=Rect(10,20,650,150)
answer_box1=Rect(20,270,300,150)
answer_box2=Rect(10,330,150,150)
answer_box3=Rect(40,30,150,150)
answer_box4=Rect(40,50,150,150)


def draw():
    screen.fill("black")
    screen.draw.filled_rect(question_box,(250, 147, 95))
    screen.draw.filled_rect(answer_box1,(3, 177, 252))
    screen.draw.filled_rect(answer_box2,(3, 177, 252))
    screen.draw.filled_rect(answer_box3,(3, 177, 252))
    screen.draw.filled_rect(answer_box4,(3, 177, 252))










pgzrun.go()