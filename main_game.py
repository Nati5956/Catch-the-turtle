#-----import statements-----
import turtle as trtl
import random as rand
#-----game configuration----
spot_color = ["orange", "pink", "black", "purple", "yellow"]
shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
score = 0

#-----initialize turtle-----
spot = trtl.Turtle()
spot.shapesize(2)
spot.shape(rand.choice(shapes))
spot.fillcolor(rand.choice(spot_color))

score_writer = trtl.Turtle()
font_setup = ("Arial", 20, "normal")
score_writer.penup()
score_writer.goto(200, 300)
score_writer.pendown()

counter =  trtl.Turtle()
counter.penup()
counter.goto(-200, 300)
counter.pendown()
timer = 15
counter_interval = 1000   #1000 represents 1 second
timer_up = False
#-----game functions--------

def spot_clicked(x, y):
    global timer_up
    if timer_up == False:
        update_score()
        change_position()
    else:
        score_writer.hideturtle()

def change_position():
    spot.penup()
    new_xpos = rand.randint(-200, 200)
    new_ypos = rand.randint(-150, 150)
    spot.goto(new_xpos, new_ypos)
    spot.pendown()

def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)

def countdown():
    global timer, timer_up
    counter.clear()
    if timer <= 0:
        counter.write("Time's Up", font=font_setup)
        timer_up = True
    else:
        counter.write("Timer: " + str(timer), font=font_setup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counter_interval)

#-----events----------------
spot.onclick(spot_clicked)

wn = trtl.Screen()
wn.bgcolor('lightblue')
wn.ontimer(countdown, counter_interval)
wn.mainloop()