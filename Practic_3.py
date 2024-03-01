'''
# Exercise №1
cost = int(input())
msv = list(str(cost))
print(msv[2])


# Exercise №2
num = int(input('Number in the range from 1 to 86400'))
hour = num//60
min = num%60
sec = (num%60)%60
print(hour,':', min)



# Exercise №3
num = int(input())
if num % 2 == 0: print('0')
else: print('1')

# Exercise №4
x, y, n = map(int, input().split())
print((x + (y/100))*n)

# Exercise №5
n = int(input())
f = ('(\___/) ')
s = ("(='.'=) ")
t = ('(\")_(\") ')
print(n*f)
print(n*s)
print(n*t)


# Exercise №6
k = int(input())
n = int(input())
r = int(input())
ks = list(str(k))
ks = ks*n
sk = ("".join(ks))
sk = int(sk)
print(sk*r)


# Exercise №7
h = 7*100
w = 5*100
way = h^2+w^2
print(way)

# Exercise №8
import turtle

def square(x, y, a, b, r):

    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.right(r)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(b)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(b)
    turtle.right(90)

turtle.speed(10)
square(0, 0, 50, 8, 0)
square(50, 0, 170, 8, 70)
square(66, -38, 300, 8, -70)
square(90, -130, 250, 8, 0)
square(110, -160, 200, 8, 0)

turtle.up()
turtle.setposition(160, -220)
turtle.down()
turtle.circle(20)

turtle.up()
turtle.setposition(280, -220)
turtle.down()
turtle.circle(20)

square(100, -43, 125, 8, 70)
square(180, -43, 125, 8, 10)
square(280, -43, 125, 8, 20)



# Exercise №10
raw = input('Enter number:')
num = str(raw)
print(num)


# Exercise №11
import math

a = int(input())
b = int(input())
c = int(input())
A = int(math.degrees(math.acos((b**2 + c**2 - a**2)/(2*b*c))))
B = int(math.degrees(math.acos((c**2 + a**2 - b**2)/(2*c*a))))
C = int(math.degrees(math.acos((a**2 + b**2 - c**2)/(2*a*b))))

print(A, B, C)


# Exercise №12
att = int(input())
comp = int(input())
yds = int(input())
td = int(input())
int = int(input())



# Exercise №13
x = int(input())
y = int(input())
print(('0', '1')[x // y * y == x])


# Exercise №14
n = float(input())




# Exercise №15
import datetime

time = datetime.datetime.now()
print(time)
'''





