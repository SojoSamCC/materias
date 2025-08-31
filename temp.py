import math
import random
import turtle as t

pantalla = t.Screen()
pantalla.title("Mi primer dicujo con turtle")
tortuga =t.Turtle()

# pi = math.pi
# for _ in range(1000000):
#     tortuga.forward(1)
#     tortuga.right(random.randint(1,random.randint(1,int(pi*pi*pi))))
#     tortuga.forward(1)

# tortuga.begin_fill()
# tortuga.circle(50)  # Dibuja un círculo
# tortuga.end_fill()

# for _ in range(10000):
# avanzar=random.randint(10,200)
# hipotenusa = math.sqrt(avanzar*avanzar+avanzar+avanzar)
# primer_angulo=random.randint(1,180)
# interno=180-primer_angulo
# segundo_angulo=interno
# tortuga.forward(avanzar)
# tortuga.right(primer_angulo)
# tortuga.forward(avanzar)
# tortuga.right(segundo_angulo)
# tortuga.forward(hipotenusa)

# t.done()

from turtle import Turtle
from random import random

t = Turtle()
for i in range(100):
    steps = int(random() * 100)
    angle = int(random() * 360)
    t.right(angle)
    t.fd(steps)

t.screen.mainloop()
