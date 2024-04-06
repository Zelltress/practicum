
# Exersize № 1:
k = 0
list = []
for i in range(100,1000):
    if i % 17 == 0:
        k += 1
        list.append(i)
print(' '.join(map(str, list)))
print(k)


# Exersize № 2:
n = input()
rslt = []
for i in range(len(n)):
    if i % 2 == 0:
        rslt.append(n[i])
print(''.join(map(str,rslt)))


# Exersize № 3
import math
while True:
    n = int(input())
    if math.isqrt(n) == True:
        print(n, '- полный квадрат')
        break
    else:
        print('Введите другое число')
        continue


# Exersize №4
num=int(input( ))
sum=0
for i in range(1, num + 1):
    sum += i
print(sum)


# Exersize №5
n = int(input())
v = 0
rslt = []
for i in range(1, n):
    if v < n-v:
        v = i**3
        rslt.append(v)
print(' '.join(map(str,rslt)))


# Exersize №6
n = int(input())
v = 1
for _ in range(1, n):
    if v < n-v:
        v *= 2
        print(v)


# Exersize №7
n = int(input())
if (n & (n-1) == 0):
    print('верно')
else:
    print('неверно')
    
    
# Exersize №8
import math
n = int(input())
print(int(math.ceil(math.log(n,2))))


# Exersize №9
n = int(input())
k = int(input())
r = int(input())
k = 0
while n < r:
    n += n*(k/100)
    k += 1
print(k)



# Exersize №10
try:
    lst = []
    while True:
        lst.append(float(input()))
except:
    print(lst)
k = 0
for i in range(1, len(lst)):
    if lst[i] < lst[i-1] or lst[i] > lst[i-1]:
        k += 1
print(k)




























