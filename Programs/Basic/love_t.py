import turtle as t 
from turtle import *
import time
win=Screen()
win.setup(1250,650)
win.title('My Cute Baby')
time.sleep(1)
win.bgcolor('white')
time.sleep(1)
a=t.Turtle()
a.color('blue','red')
a.shape('arrow')
a.penup()
time.sleep(1)
a.goto(-600,250)
a.width(8)


def curve(): 
	for i in range(200): 
		a.right(1) 
		a.forward(1) 



def heart(): 
	a.fillcolor('red')  
	a.begin_fill() 
	a.left(140) 
	a.forward(113)
	win.bgcolor('#ffcccc')
	curve() 
	a.left(120) 
	curve() 
	a.forward(112) 
	a.end_fill() 
 
a.penup()
a.setpos(0,-100) 
a.pendown()
a.width(4)
a.shape('turtle')
a.color('white','yellow')
heart()


pen=t.Turtle('classic')
def txt():
	pen.up()
	pen.setpos(-600,95)
	pen.down()
	pen.color('deep pink')
	pen.write('\u2764\ufe0f \u2764\ufe0f \u2764\ufe0f Hii Baby \u2764\ufe0f \u2764\ufe0f \u2764\ufe0f', font=("Courier",15,"italic"))
	time.sleep(1.5)
	
win.title('My Cute Baby -  I \u2764\ufe0f U ')
txt()
win.bgcolor('#ecb3ff')
win.mainloop()