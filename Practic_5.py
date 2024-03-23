# Exersize №1
year = int(input())
if year % 4 == 0:
    print('366')
else:
    print('365')


# Exersize №2
import matplotlib.pyplot as plt

xc = int(input())
yc = int(input())
r = int(input())
x = int(input())
y = int(input())

figure, axes = plt.subplots()
circle = plt.Circle((xc, yc), r)
plt.xlim(-200, 200)
plt.ylim(-200, 200)
plt.plot(x, y)
axes.add_artist(circle)

if (x - xc) ** 2 + (y - yc) ** 2 < r ** 2:
    print('точка внутри окружности')
else:
    print('точке вне окружности')
plt.show()


# Exersize №3
num = int(input())
frst = num // 100
scnd = (num % 100) // 10
thrd = num % 10

if frst == thrd * 10 + scnd:
    print('настоящее')

else:
    print('кривое')


# Exersize №4
n = int(input())
declination = {1: 'папугай', 2: 'попугая', 5: 'попугаев'}
if n == 1 or (n > 20 and (n % 10) == 1):
    print(n, declination[1])
elif (n > 1 and n < 5) or (n > 20 and (n % 10) > 1 and (n % 10) < 5):
    print(n, declination[2])
else:
    print(n, declination[5])


# Exersize №5
wt_kg = int(input())
ht_cm = int(input())
indx = wt_kg / ((ht_cm / 100) ** 2)
if indx < 16:
    print('выраженный дефицит массы тела')
elif 16 <= indx < 18.5:
    print('недостаточная масса тела')
elif 18.5 <= indx < 25:
    print('норма')
elif 25 <= indx < 30:
    print('избыточная масса тела')
elif 30 <= indx < 35:
    print('ожирение первой степени')
elif 35 <= indx < 40:
    print('ожирение второй степени')
else:
    print('ожирение третьей степени')


# Exersize №6
day = list(map(int, input().split()))
check = 0
for i in day:
    if day.count(i) > 1:
        check += 1
print(check)


# Exersize №7
n, k, m = map(int, input().split())
if (n - m) < abs(k - m):
    print((n - m) - 1)
else:
    print(abs(k - m) - 1)


# Exersize №8
lst = []
n = int(input())
skl = n // 29
if skl % 17 == 0:
    gl = skl // 17
    lst.append(gl)
    skl = 0
if n - gl != 0:
    kn = n - gl * 17 * 29
    if kn != 0:
        lst.append(kn)
if skl != 0:
    lst.append(skl)
print(lst)


# Exersize №9
high = list(map(int, input().split()))
frst = max(high)
thrd = min(high)
high.remove(frst)
high.remove(thrd)
scnd = high[0]
print(frst, scnd, thrd)


# Exersize №10
pin = list(map(int, input()))
for i in pin:
    for j in range(i + 1, pin[3]):
        if pin[i] == pin[j]:
            print('ERROR')
if len(pin) > 4:
    print('ERROR')
elif 1 <= pin[0] <= 2 and (pin[1] == 9 or pin[1] == 0):
    print('ERROR')
else:
    print('OK')
