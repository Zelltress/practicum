# Exercise №1
code = input()
if code == 'пароль':
    print('Проходи!')
else:
    print('Доступ запрещен!')


# Exercise №2
wrds = input('Какие два слова передал первой радиограммой Александр Попов? ').split()
frst_wrd = 'примите'
scnd_wrd = 'радиограмму'
print(wrds[0] == frst_wrd)
print(wrds[1] == scnd_wrd)



# Exercise №3
answer = 'Джеймс Бонд'
while True:
    user_wrd = str(input('Как зовут главного персонажа романа Яна Флеминга о '
             'вымышленном шпионе секретной разведывательной службы Великобритании? '))
    if user_wrd.lower() == answer.lower():
        print('Верно')
    else:
        print('Неверно')
        continue



# Exercise №4
answer = ['да', 'нет']
while True:
    user_wrd = str(input('Вы поедете на бал? '))
    if user_wrd.lower() != answer[0].lower() and user_wrd != answer[1].lower():
        print('Верно')
    else:
        print('Неверно')
        continue



# Exercise №5
frst_fisherman = int(input())
scnd_fisherman = int(input())
if frst_fisherman < scnd_fisherman:
    print(frst_fisherman)
elif scnd_fisherman < frst_fisherman:
    print(scnd_fisherman)
else:
    print('Одинаковый улов')



# Exercise №6
frst_team, scnd_team = map(int, input().split(':'))
if frst_team < scnd_team:
    print(1)
elif scnd_team < frst_team:
    print(2)
else:
    print(0)
    
    

# Exercise №7
players = list(map(int, input().split()))
max = players[0]
for i in range(1, len(players)):
    if players[i] > max:
        max = players[i]
print(max)



# Exercise №8
answer = ['да', 'нет']
name = input('Здравствуйте! Как Вас зовут? ')
print('Очень приятно,', name, ' Меня зовут Марк.', sep="")

age = int(input('Сколько Вам лет? '))
if age < 78:
    print('Да, ', name, ', я старше Вас на ', abs(78-age), ' лет.', sep="")
else:
    print('Да, ', name, ', Вы старше меня на ', abs(78-age), ' лет.', sep="")

user_wrd = input('Вам нравится программировать? ')
if user_wrd.lower() == answer[0].lower():
    print('Превосходно! Уверен, у Вас получится написать множество полезных'
          'и хороших программ'.)
else:
    print('Жаль. Я думал, Вы сможете написать интересную программу для меня.')



# Exercise №9
a = 'да'
if a == str(input('Собака короткошерстой породы? ')):
    if a == str(input('Рост собаки менее 50см? ')):

        if a == str(input('У собаки короткий хвост? ')):
            print('английский бульдог')
        elif a == str(input('У собаки длинные уши? ')):
            print('гончая')
        elif a == str(input('У собаки короткое тело? ')):
            print('мопс')
        else:
            print('чихуахуа')

    elif a == str(input('Собака весит более 50кг? ')):
        print('датский дог')
    else:
        print('фоксхаунд')

elif a == str(input('Рост собаки менее 50см? ')):
    if a == str(input('У собаки доброжелательный характер? ')):
        print('кокер-спаниель')
    else:
        print('ирландский сеттер')

elif a == str(input('У собаки рост менее 70см? ')):
    if a == str(input('У собаки длинные уши? ')):
        print('большой вандейский грифон')
    else:
        print('колли')

elif a == str(input('Окрас рыжий с белыми отметинами? ')):
    print('сенбернар')

elif a == str(input('Белоснежный окрас? ')):
    print('ирландский волкодав')

else:
    print('ньюфаундленд')



# Exercise №10
number = int(input())
if number % 2 == 0:
    print('да')
else:
    print('нет')

