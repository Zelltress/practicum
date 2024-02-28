# Exercise №1
total_cost = int(input())

quantity_ag = 96
quantity_au = quantity_ag / 16
sold_ag = quantity_ag * 48
sold_au = total_cost - sold_ag
cost_au = sold_au / quantity_au
cost_au = int(cost_au)
print(cost_au)

# Exercise №2
name = str(input()).split(',')
print(*name, sep='\n')

# Exercise №3
s, r = map(int, input().split())
print(s + r)

# Exercise №4
ppl = 1 + 1 + 7
cats = 7 ** 4 + 7 ** 3
print(cats + ppl)

# Exercise №5
plnd_amnt = float(input())
profit = 0.19 * plnd_amnt
print(profit)

# Exercise №6
wt_pd = int(input())
ht_dm = int(input())
wt_kg = wt_pd * 0.45359237
ht_cm = ht_dm * 2.54
indx = wt_kg / (ht_cm ** 2)
print(indx)

# Exercise №7
ha = int(input())
rain = int(input())
v = ha * (10 ** 8) * rain
print(v)

# Exercise №8
n, m = map(int, input().split())
print(m // (n + 1))

# Exercise №9
n = int(input())
k = int(input())
bull = n % k
print(bull)

# Exercise №10
m = int(input())
ml = m * 0.00062
print(int(ml))
