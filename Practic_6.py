
# Exersize 1
r = float(input())
n, k = map(int, input().split('x'))
crcl = r*2
pr = n*k
if crcl > pr:
    print('yes')
else:
    print('no')


# Exersize 2
h, w = map(int, input().split('x'))
c, d, e = map(int, input().split('x'))
if h*w >= (c*d or d*e or c*e):
    print('yes')
else:
    print('no')


# Exersize 3
n, m = map(int, input().split('x'))
k = int(input())
if n*m % 2 == 0 and k % 2 == 0:
    print('yes')
else:
    print('no')



# Exersize 4
letter = input()
n = int(input())

letters = {'a': 1,'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
num = list(range(1, 10))

if letters[letter] % 2 == num.index(n) % 2:
    print('white')
else:
    print('black')


# Exersize 5
y_1 = input()
x_1 = int(input())
y_2 = input()
x_2 = int(input())

letters = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
num = list(range(1, 10))

if (x_1 - 1 == x_2 or x_1 + 1 == x_2) and (letters[y_1] - 2 == letters
[y_2] or letters[y_1] + 2 == letters[y_2]):
    print('yes')
elif (x_1 - 2 == x_2 or x_1 + 2 == x_2) and (letters[y_1] - 1 == letters[y_2] or letters[y_1] + 1 ==
                                             letters[y_2]):
    print('yes')
else:
    print('no')


# Exersize 6
n, k, m = map(int, input().split())
c = 0
for i in range(n):
    c += m
print(2*c)


# Exersize 7
n = int(input())
k = 0
for i in range(n+1):
    n = n-7
    if n % 5 == 0:
        k += 1
    else:
        continue
if k > 0:
    print('yes')
else:
    print('no')



# Exersize 9
import matplotlib.pyplot as plt

xc_1 = int(input())
yc_1 = int(input())
xc_2 = int(input())
yc_2 = int(input())
r_1 = int(input())
r_2 = int(input())

figure, axes = plt.subplots()
circle_1 = plt.Circle((xc_1, yc_1), r_1)
circle_2 = plt.Circle((xc_2, yc_2), r_2)
plt.xlim(-200, 200)
plt.ylim(-200, 200)
axes.add_artist(circle_1)
axes.add_artist(circle_2)

if (xc_1 - xc_2) ** 2 + (yc_1 - yc_2) ** 2 < r_2 ** 2:
    print('Одна окружность лежит внутри другой, не касаясь')
elif (xc_1 - xc_2) ** 2 + (yc_1 - yc_2) ** 2 <= r_2 ** 2:
    print('Окружности имеют внутреннее касание')
elif (xc_2 - xc_1) ** 2 + (yc_2 - yc_1) ** 2 < r_2 ** 2:
    print('Окружности лежает одна вне другой, не касаясь')
elif (xc_2 - xc_1) ** 2 + (yc_2 - yc_1) ** 2 <= r_2 ** 2:
    print('Окружности имеют внешнее касание')
else:
    print('Окружности пересекаются')

plt.show()
