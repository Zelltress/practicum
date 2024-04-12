# Exercise №1
try:
    lst = []
    while True:
        lst.append(int(input()))
except:
    print(lst)
max = 0
for i in range(len(lst)):
    if lst[i] > lst[i-1]:
        max = lst[i]
print(max)



# Exercise №2
try:
    lst = []
    while True:
        lst.append(int(input()))
except:
    print(len(lst))



# Exercise №3
try:
    lst = []
    while True:
        lst.append(float(input()))
except:
    print(lst)
avrg = 0
for i in range(len(lst)):
    avrg += lst[i]

avrg = avrg/len(lst)
print(round(avrg, 1))



# Exercise №4
num = int(input( ))
sum = 0
for i in range(1, num + 1):
    sum += i
    print(sum)



# Exercise №5
n = int(input())
k = 0
for i in range(1, n):
    sum = 0
    for j in range(1, i):
        if i % j == 0:
            sum += j
    if sum == i:
        k += 1
print(k)



# Exercise №6
n = int(input())
for i in range(n+1):
    print((' '*(n-i)) + ('*'*(i)))



# Exercise №7
while True:
    try:
        n = int(input('Введите число: '))
    except:
        print('Ошибка. Попробуйте ещё раз.')



# Exercise №8.1
r = '123456789'
k = '987654321'
for i in range(1, 10):
        print(r[:i], '* 8 +', i ,'=', k[:i])



# Exercise №8.2
r = '123456789'
k = '111111111'
for i in range(1, 10):
        print(r[:i], '* 9 +', i ,'=', k[:i])



# Exercise №8.3
def times(n):
  return ['1'*k for k in range(1, n+1)]

for x in times(10):
  print(f'{x} x {x} = {int(x)**2}')



# Exercise №9
n = int(input())
num = [i for i in range(n+1)]
num[1] = 0
i = 2
while i <= n:
    if num[i] != 0:
        j = 2 * i
        while j <= n:
            num[j] = 0
            j += i
    i += 1
num = [i for i in num if i != 0]
print(num)



# Exercise №10
n = int(input())
k = 0
for i in range(1, n):
    sum = 0
    for j in range(1, i):
        if i % j == 0:
            sum += j
    if sum == i:
        print(i)



