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
else: print('1')???????????????????????????

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
'''

# Exercise №8
import turtle

def square(x, y, a):

    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)






