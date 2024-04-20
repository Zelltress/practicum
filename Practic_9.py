# Exersize 1
n, d, r = map(int, input().split(' '))
print(2*r*n + 2*d)



# Exersize 2
import math
n = int(input('Enter a number greater than 2: '))
while n > 2:
    n = math.sqrt(n)
    print("{0:.3f}".format(n))



# Exersize 3
n = int(input())
min = n
for i in range (1, n):
    if n % i == 0 and i < min and i > 2:
        min = i
print(min)



# Exersize 4
try:
    lst = []
    while True:
        lst.append(int(input()))
except:
    print(lst)
k = 0
for i in range(len(lst)):
    if lst[i]%2 == 0:
        k += 1
print(k)



# Exersize 5
n = 100000
rs = []
rs_1 = []
rs_2 = []

for i in range(n, 999999):
    lst = list(map(int, str(i)))
    if lst[1] == lst[5] and lst[2] == lst[4] and lst[1] != 0:
        rs.append(i)

        for j in rs:
            if lst[1] == lst[4] and lst[2] == lst[3] and lst[1] != 0:
                rs_1.append(j)

                for l in rs_1:
                    if lst[0] == lst[5] and lst[1] == lst[4] and lst[2] == lst[3]:
                        rs_2.append(j)
print(rs_2)



# Exersize 6
for ab in range(10, 99):
    for c in range(100, 999):
        if ab**2 == c:
            print(ab)



# Exersize 7
def decision():
    res = []
    for s in range(9, -1, -1):
        for e in range(9, -1, -1):
            for n in range(9, -1, -1):
                for d in range(9, -1, -1):
                    for m in range(9, 0, -1):
                        for o in range(9, -1, -1):
                            for r in range(9, -1, -1):
                                for y in range(9, -1, -1):
                                    if len(set([s, e, n, d, m, o, r, y])) == 8:
                                        send = 1000 * s + 100 * e + 10 * n + d
                                        more = 1000 * m + 100 * o + 10 * r + e
                                        money = 10000 * m + 1000 * o + 100 * n + 10 * e + y

                                        if send + more == money:
                                            res.append((send, more, money))
    return res

print(decision())



# Exersize 8
x = int(input())
k = 0
for i in range (1, 100):
    for j in range(1, 100):
        if x == i**2 + j**2:
            k += 1
print(k/2)



# Exersize 9
n = int(input())
sum = 0
for i in range(0, n+1):
    for j in range(0, i+1):
        sum += (i + j)
        print(i, j)
print(sum)



# Exersize 10
n = ((int(input()) * 2) ** 0.5) - 0.4
print(int(n)+1)
