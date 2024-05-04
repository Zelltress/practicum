# Exercise 1
with open('input.txt', 'r', encoding='utf-8') as f:
    while c := f.read(1):
        with open('output.txt', 'a', encoding='utf-8') as g:
            print(c.upper(), end='', file=g)


# Exercise 2
with open('input.txt', 'r') as frst_f, open('output.txt', 'a') as scnd_f:
    text = frst_f.readlines()
    for i in (text):
        if i == 'a' or i == 'A':
            scnd_f.write(i)


# Exercise 3
with open('input.txt', 'r') as frst_f, open('output.txt', 'a') as scnd_f:
    while text := frst_f.readline():
        c = text[0]
        scnd_f.write(c)



# Exercise 4
with open('input.txt', 'r') as frst_f, open('output.txt', 'a') as scnd_f:
    while text := frst_f.readline():
        if len(text) > 20:
            scnd_f.write(text)



# Exercise 5
try:
    with open('input.txt', 'r') as frst_f, open('output.txt', 'a') as scnd_f:
        a = 0
        for x in frst_f:
            a += int(x)
        scnd_f.write(str(a))
except ZeroDivisionError:
    print('One of the arguments is zero')
except ValueError:
    print('Incorrect value')



# Exercise 6
with open('input.txt', 'r') as frst_f:
    try:
        x = frst_f.read(1)
        int(x)
        k = 1
        for i in frst_f:
            line = frst_f.readline()
            k += 1
        if k == x:
            print("YES")
        else:
            print("NO")
    except ValueError:
        print('ERROR')



# Exercise 7
with (open('input.txt', 'r')) as frst_f:
    lines = frst_f.readlines()
with (open('input.txt', 'a')) as frst_f:
    ch = '100\n'
    for x in lines:
        if ch not in x:
            frst_f.write(x)



# Exercise 9
with open('input.txt', 'r') as f, open(r'simple/output.txt', 'w') as s:
    res = ''
    i = 1
    for line in f.readlines():
        if i % 2 == 0:
            res += line
        i += 1
    s.write(res)
        


# Exercise 10
def date_moth(month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 28


def date_days(date, current_date):
    day1, month1 = map(int, date.split('.'))
    day2, month2 = current_date
    if month2 < month1:
        month2 = month2 + 12
    return (month2 - month1) * 31 + day2 - day1


def check_storage(input_file, output_file):
    with open(input_file, 'r') as f:
        current_date = list(map(int, f.readline().strip().split('.')))
        n = int(f.readline().strip())
        storage = []
        for _ in range(n):
            cell, date = f.readline().strip().split()
            storage.append((int(cell), date))

    result = [cell for cell, date in storage if date_days(date, current_date) > 3]

    with open(output_file, 'w') as f:
        for cell in result:
            f.write(str(cell) + '\n')


check_storage('input.txt', 'output.txt')







