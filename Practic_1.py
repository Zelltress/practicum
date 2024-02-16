#Practicum №1 
#Cherkashina D.

#Exercize №1
print ('Hello, Python!')


#Exercize №2
print("""
Привет, Python!
Hello, Python!
Bonjour Python!
Hej, Python!
Hola, Python!
""")


#Exercize №3
print('Привет', end=' ')
print('Python!')


#Exercize №4
print ("""
(\___/)
(='.'=)
(")_(")
""")


#Exercize №5
print(' Привет, Python! \n Hello, Python! \n Bonjour Python! \n Hej, Python! \n Hola, Python!')


#Exercize №6
name = input('What is your name?: ')
print('Hello,', name)


#Exercize №7
name = input('What is your name? ')
print('Hello,', name)
sport = input('What do you like? ')
print('Great!', sport, 'are a good hobby.')


#Exercize №8
lg = input('Login: ')
ps = input('Password: ')
ps_new = input('New password: ')
if ps != ps_new:
    print('User', lg, 'has changed the password to', ps_new)
else:
    print('The passwords match')


#Exercize №9
music = input('Enter the playlist separated by a commas ').split(',')
music.reverse()
print ('\n'.join(music))


#Exercize №10
number = input('flight number: ')
name_ru = input('airline name (in russian): ')
name_en = input('airline name (in english): ')
town_ru = input('arrival city (in rus): ')
town_en = input('arrival city (in en): ')
print('Заканчивается посадка на рейс', number, 'авиакомпании',
      name_ru, 'до', town_ru)
print('This is the final boarding call for', name_en,
      'Airlines flight', number, 'to', town_en)


#Exercize №11
nm = input('What is your name? ' )
print('Hello there, ', nm, '!', sep="")


#Exercize №12
quantity_ag = int(input())
total_cost= int(input())

quantity_au = quantity_ag/16
sold_ag = quantity_ag*48
sold_au = total_cost-sold_ag
cost_au = sold_au/quantity_au
print(cost_au)


#Exercize №13
import math

blinde_spot = int(input())
reception_rage = int(input())

crcl_blnd_spot = math.pi*(blinde_spot**2)
crcl_rcptn_rage = math.pi*(reception_rage**2)

coverage_area = abs(crcl_rcptn_rage-crcl_blnd_spot)
print(coverage_area)


#Exercize №14
n = int(input())
print(((n+2)*3-6)/3-4)


#Exercize №15
cm = float(input())
inch = cm/2.54
ft = inch/12
yd = ft/3
ml = yd/1760
print(inch, ft, yd, ml)














