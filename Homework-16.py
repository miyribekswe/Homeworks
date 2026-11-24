#1 tapsirma
number = [10, 20, 30, 40, 50]

print(number[0])
print(number[2])
print(number[4])


#2 tapsirma


#3 tapsirma
colors = ['red', 'green', 'blue', 'yellow']

colors[1] = 'black'
colors[3] = 'white'

print(colors)


#4 tapsirma
students = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']

print(len(students))


#5 tapsirma
numbers = [10, 20, 30, 40, 50, 60, 70, 80]

print(numbers[2:5])


#6 tapsirma
letters = ['a', 'b', 'c', 'd', 'e', 'f']

print(letters[::-1])


#7 tapsirma
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(numbers[::2])


#8 tapsirma
students = [
    ['Ali', 90, 'English'],
    ['Vali', 85, 'Math'],
    ['Hasan', 95, 'Python']
]

print(students[0][0])
print(students[0][1])
print(students[0][2])


#9 tapsirma
students = [
    ['Ali', 90],
    ['Vali', 85],
    ['Hasan', 95]
]

students[0][1] = 100

print(students)


#10 tapsirma
programming = [
    ['HTML', 'CSS'],
    ['Python', 'JavaScript'],
    ['Java', 'C++']
]

print(programming[1][0])
print(programming[1][1])


#11 tapsirma
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(numbers[1::3])


#12 tapsirma
numbers = [12, 7, 8, 15, 20, 33, 44, 51, 60]

numbers1 = [12, 8, 20, 44, 60]

print(numbers1)


#13 tapsirma
numbers = [1, 2, 3, 2, 4, 1, 5, 3, 6]

numbers1 = [1, 2, 3, 4, 5, 6]

print(numbers1)


#14 tapsirma
numbers = [10, 20, 30, 40, 50, 60, 70, 80]

list1 = numbers[:4]
list2 = numbers[4:]

print(list1)
print(list2)


#15 tapsirma
numbers = [10, 20, 30, 40, 50]

numbers[1], numbers[3] = numbers[3], numbers[1]

print(numbers)


#16 tapsirma
students = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']

students[0], students[4] = students[4], students[0]

print(students)


#17 tapsirma
students = [
    ['Ali', 85],
    ['Vali', 90],
    ['Hasan', 75],
    ['Husan', 95]
]

students[0], students[2] = students[2], students[0]

print(students)


#18 tapsirma
fruits = ['Olma', 'Uzum', 'Banan', 'Anor', 'Shaftoli']

print("Meyweler:")
print("1.", fruits[0])
print("2.", fruits[1])
print("3.", fruits[2])
print("4.", fruits[3])
print("5.", fruits[4])

tanlaw = int(input("Qaysi mewani tanlaysiz? "))

print("Siz", fruits[tanlaw - 1], "mewesin tanladingiz!")


#19 tapsirma
fruits = ['Olma', 'Uzum', 'Banan', 'Anor', 'Shaftoli']
prices = [5, 8, 12, 10, 15]

print("========== FRUIT MARKET ==========")

print("1. Olma - 5$")
print("2. Uzum - 8$")
print("3. Banan - 12$")
print("4. Anor - 10$")
print("5. Shaftoli - 15$")

tanlaw = int(input("Qaysi mewani tanlaysiz? "))

print("Meva:", fruits[tanlaw - 1])
print("1 kg bahasi:", prices[tanlaw - 1], "$")

kg = float(input("Neshe kg alasiz? "))

print("========== CHEK ==========")
print("Meva:", fruits[tanlaw - 1])
print("Miqdori:", kg, "kg")
print("1 kg narxi:", prices[tanlaw - 1], "$")
print("Ulıwma narx:", prices[tanlaw - 1] * kg, "$")
print("Xaridingiz ushın raxmet!")


#20 tapsirma
fruits = ['apple', 'banana', 'orange']

fruits.append('mango')
fruits.insert(2, 'strawberry')

print(fruits)


#21 tapsirma
cars = ['BMW', 'Mercedes', 'Audi', 'Tesla']

cars.remove('BMW')

print(cars)


#22 tapsirma
numbers = [10, 20, 30, 40, 50]

print("Ochirilgan element:", numbers.pop())
print("Qolgan list:", numbers)


#23 tapsirma
fruits = ['apple', 'banana', 'apple', 'orange', 'apple', 'kiwi']

print("apple soni:", fruits.count('apple'))


#24 tapsirma
languages = ['Java', 'C++', 'Python', 'JavaScript', 'PHP']

print("Python indeksi:", languages.index('Python'))


#25 tapsirma
numbers = [45, 12, 89, 3, 21, 67, 10]

numbers.sort()

print(numbers)
