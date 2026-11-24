#T-1
fruits = ['apple', 'banana', 'orange', 'kiwi']
for i in fruits:
    print(i)


#T-2
names = ['ali', 'vali', 'hasan', 'husan']
for i in names:
    print(i.upper())


#T-3
cars = ['bmw', 'mers', 'nexia', 'malibu', 'cobalt']
for i in cars:
    print(i[0])


#T-4
countries = ['UZBEKISTAN', 'RUSSIA', 'TURKEY', 'USA']
for i in countries:
    print(i.lower())
#T-5
names = ['ali', 'sardor', 'abdulloh', 'aziz']
for i in names:
    print(f'{i} - {len(i)} ta harf')


#T-6
animals = ['cat', 'dog', 'lion', 'tiger']
for i in range(4):
    animals[i] = animals[i].upper()
print(animals)


#T-7
names = ['ali', 'vali', 'sardor', 'aziz']
for i in range(4):
    names[i] = names[i].upper()
print(names)


#T-8
names = ['ali', 'hasan', 'husan', 'sardor']
for i in range(4):
    names[i] = names[i].capitalize()
print(names)
#T-9
names = ['ali', 'vali', 'hasan', 'husan', 'sardor', 'aziz']
for i in range(0, 6, 2):
    print(names[i])


#T-10
animals = ['tiger', 'lion', 'elephant', 'rabbit']
for i in animals:
    print(i[0], '-', i[-1])


#T-11
words = ['python', 'programming', 'computer', 'developer']
for i in range(len(words)):
    words[i] = words[i].capitalize()
print(words)


#T-12
cars = ['bmw', 'nexia', 'malibu', 'cobalt', 'damas']
for i in range(0, 5):
    cars[i] = cars[i].upper()
print(cars)
#T-13
ism = input('Ism kiriting: ')
necha_marta = int(input('Necha marta chiqarilsin: '))
for i in range(necha_marta):
    print(ism)


#T-14
meyveler = []
necha = int(input('Nechta meva kiritmoqchisiz: '))
for i in range(necha):
    meyve = input(f'{i+1}-mevani kiriting: ')
    meyveler.append(meyve)

print('Meyvalar:', meyveler)


#T-15
renler = []
for i in range(5):
    renk = input(f'{i+1}-rangni kiriting: ')
    renler.append(renk)

print('\nSizning sevimli ranglaringiz:')
for i in renler:
    print(i)
