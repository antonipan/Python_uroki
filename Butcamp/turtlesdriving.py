from random import randint
from turtle import *
from time import *

finish = 200

colors = ["red", "green", "blue", "yellow", "black", "orange"]
phrases = ["Ай!", "Больно!", "Хватит!", "Прекрати!"]
turtles = []

for i in range(4):
    turtles.append(Turtle(shape='turtle', speed = 3)) #создание объекта, присвоение вида и скорости
    turtles[i].color(colors.pop(randint(0, len(colors) - 1))) #присвоение цвета и удаление его из списка
    turtles[i].penup() #поднятие(не рисует)
    turtles[i].goto(-200,-60 + (i * 25)) #перемещение
    turtles[i].pendown() #опускание(возможность рисовать)

def razmetka(): #функция рисует разметку поля
    t = Turtle()
    t.speed(0)
    for i in range(1, 21):
        t.penup()
        t.goto(-200 + i * 20, 50)
        t.pendown()
        t.goto(-200 + i * 20, -100)
        t.hideturtle()

# это первый вариант, который я хочу улучшить
def catch(x, y, i): #обработчик события нажатия
    i.write(phrases[randint[0, len(phrases) - 1]], font = ('Arial', 14, 'normal'))
    i.fd(randint(10, 15))

turtles.onclick(catch(turtles[i]))

# второй вариант, который можно улучшить, но не знаю как
def catch(x, y, i): #обработчик события нажатия
    turtles[i].write(phrases[randint[0, len(phrases) - 1]], font = ('Arial', 14, 'normal'))
    turtles[i].fd(randint(10, 15))

turtles[0].onclick(catch())
turtles[1].onclick(catch())
turtles[2].onclick(catch())
turtles[3].onclick(catch())

razmetka()

while True:
    exit_flag = False
    for i in turtles:
        if i.xcor() >= finish:
    exit_flag = True
        if exit_flag: break
    for i in turtles:
        i.forward(randint(2, 5))
        sleep(0.01)