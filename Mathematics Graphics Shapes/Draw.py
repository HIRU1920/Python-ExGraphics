import turtle
import math
turtle.up()
tk=turtle.Turtle()
tk.speed(0)
turtle.hideturtle()
val=turtle.textinput('input (in mm)',"enter the distance of focus from directrix:")
val=float(val)*2
ec=turtle.textinput('input (numarator/denominator)',"enter ecentricity:")
num,den=ec.split('/')
num,den=int(num),int(den)
check=True
if num<den:
	check=False
tk.up()
tk.goto(-280,0)
tk.down()
tk.pencolor('lemon chiffon')
tk.lt(90)
orgpos=tk.pos()
tk.fd(400)
tk.back(800)
tk.fd(400)
tk.rt(90)
tk.fd(600)
tk.back(600)
tk.pencolor('tomato')
tk.fd(val)
fx=tk.xcor()
turtle.goto(tk.pos())
turtle.write('f')
tk.pencolor('lemon chiffon')
turtle.goto(tk.pos())
turtle.dot(10)
tk.up()
tk.back((val*num)/(num+den))
vpos=tk.pos()
turtle.goto(vpos)
turtle.write('v')
turtle.dot(10)
tk.lt(90)
tk.fd((val*num)/(num+den))
turtle.goto(tk.pos())
turtle.dot(10)
tk.back((val*num)/(num+den))
tk.rt(90)
lis=[]
for i in range(20):
	tk.fd(25)
	lis.append(tk.xcor())
	tk.down()
	tk.lt(90)
	tk.fd(400)
	tk.back(800)
	tk.fd(400)
	tk.rt(90)
	tk.up()
tk.goto(-280,0)
tk.down()
tk.seth(0)
deg=math.degrees(math.atan((val*num)/(val*den)))
tk.lt(deg)
k=0
tk.fd(700)
tk.up()
tk.goto(vpos)
tk.seth(0)
tk.down()
x,y=vpos
lisy=[]
z=False
ox,oy=orgpos
tk.pencolor('black')
ratio=num/den
lim=0
tk.hideturtle()
while True:
	y=(abs(x-ox))*ratio
	y=math.sqrt(abs((y**2)-((x-fx)**2)))
	tk.goto(x,y)
	print(x,y)
	lisy.append(y)
	x+=1
	if (int(y)==0 and z) or (lim>=300 and check):
		break
	z=True
	if check:
		lim+=1
if check:
	tk.up()
lisy.reverse()
for i in lisy:
	x-=1
	tk.goto(x,(-i))
	tk.down()
turtle.mainloop()