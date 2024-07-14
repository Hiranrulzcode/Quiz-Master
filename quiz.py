import pgzrun

WIDTH=870
HEIGHT=650
TITLE="Quiz Master"

question_box=Rect(10,20,650,150)
answer_box1=Rect(20,200,300,150)
answer_box2=Rect(20,420,300,150)
answer_box3=Rect(350,200,300,150)
answer_box4=Rect(350,420,300,150)
timer_box=Rect(680,20,150,150)
skip_box=Rect(680,200,150,420)

answer_boxes=[answer_box1, answer_box2, answer_box3, answer_box4]

time_left=10
score=0
question_file_name="questions.txt"
is_game_over=False
questions=[]
question_count=0
question_index=0



def draw():
    screen.fill("black")
    screen.draw.filled_rect(question_box,(250, 147, 95))
    screen.draw.filled_rect(timer_box,(7, 245, 138))
    screen.draw.filled_rect(skip_box,(48, 112, 2))

    for answer_box in answer_boxes:
        screen.draw.filled_rect(answer_box,(3, 177, 252))

    screen.draw.textbox(str(time_left),timer_box, color="black")
    screen.draw.textbox("skip",skip_box,color="black",angle=-90)
    screen.draw.textbox(question[0].strip(),question_box,color="black")
    index=1
    for answer_box in answer_boxes:
        screen.draw.textbox(question[index].strip(),answer_box,color="black")
        index=index+1


def update():
    pass


def read_question_file():
    global question_count, questions
    q_file=open(question_file_name, "r")

    for question in q_file:
        questions.append(question)
        question_count=question_count+1

    q_file.close()


    

read_question_file()
print(questions)

def read_next_question():
    global question_index
    question_index=question_index+1
    return questions.pop(0).split(",")

question=read_next_question()

def update_time_left():
    global time_left
    if time_left:
        time_left=time_left-1

clock.schedule_interval(update_time_left, 1)

def on_mouse_down(pos):
    index=1
    for box in answer_boxes:
        if box.collidepoint(pos):
            if index is int(question[5]):
                correct_answer()
            else:
                #game_over()
                neg_score()
        index=index+1
    if skip_box.collidepoint(pos):
        skip_question()

def correct_answer():
    global score, question, time_left, questions
    score=score+1
    if questions:
        question=read_next_question()
        time_left=10
    else:
        game_over()

def skip_question():
    global question, time_left
    if questions:
        question=read_next_question()
        time_left=10

def game_over():
    global question, time_left, is_game_over
    message=f"Game over!\nYou got{score}questions correct!"
    question=[message,"-","-","-","-",0]
    time_left=0
    is_game_over=True

def neg_score():
    global score, question, time_left
    score=score-1
    if questions:
        question=read_next_question()
        time_left=10


pgzrun.go()