#list elementin ozgertiw
#T-1
jasi = int(input("Yoshingizni kiriting: "))

if jasi >= 18:
    print("Siz voyaga yetgansiz!")
else:
    print("Siz voyaga yetmagansiz!")


#T-2
parol = input("Parolni kiriting: ")

if parol == "python123":
    print("Xush kelibsiz!")
else:
    print("Parol notogri!")


#T-3
baha = int(input("Mahsulot narxini kiriting: "))

if baha > 500000:
    chegirma = baha * 10 / 100
else:
    chegirma = 0

yakuniy = baha - chegirma

print("Chegirma:", chegirma, "so'm")
print("Yakuniy narx:", yakuniy, "so'm")


#T-4
araliq = int(input("Araliqni kiriting: "))

if araliq > 10:
    narx = 3000
else:
    narx = 2000

umumiy = araliq * narx

print("1 km bahasi:", narx, "swm.")
print("Ulıwma bahasi:", umumiy, "sum.")
#T-5
buyurtpa = int(input("Buyurtpa bahasi: "))

if buyurtpa > 100000:
    print("Jetkiriw biypul!")
    print("Jami tolem:", buyurtpa, "sum.")
else:
    jami = buyurtpa + 15000
    print("Jetkerip beriw: 15000 sum.")
    print("Jami tolem:", jami, "sum.")


#T-6
ball = int(input("Ballingizni kiriting: "))

if ball >= 90:
    print("Sizning bahoyingiz: A'lo")
elif ball >= 75:
    print("Sizning bahoyingiz: Yaxshi")
elif ball >= 60:
    print("Sizning bahoyingiz: Qoniqarli")
else:
    print("Sizning bahoyingiz: Qoniqarsiz")


#T-7
transportlar = ["Avtobus", "Metro", "Taksi", "Velosiped"]
narxlar = [2000, 1700, 15000, 1000]

print("===== TRANSPORT TANLASH =====")
print("1. Avtobus")
print("2. Metro")
print("3. Taksi")
print("4. Velosiped")

tanlaw = int(input("Transportni tanlang: "))

if tanlaw == 1:
    print("Siz Avtobus transportini tanladingiz.")
    print("Narxi:", narxlar[0], "so'm")
elif tanlaw == 2:
    print("Siz Metro transportini tanladingiz.")
    print("Narxi:", narxlar[1], "so'm")
elif tanlaw == 3:
    print("Siz Taksi transportini tanladingiz.")
    print("Narxi:", narxlar[2], "so'm")
elif tanlaw == 4:
    print("Siz Velosiped transportini tanladingiz.")
    print("Narxi:", narxlar[3], "so'm")
else:
    print("Bunday transport mavjud emas!")
#T-8
mevalar = ["olma", "banan", "uzum", "anor", "shaftoli"]

meva = input("Meva nomini kiriting: ")

if meva in mevalar:
    print(meva, "ro'yxatda mavjud!")
else:
    print(meva, "ro'yxatda mavjud emas!")


#T-9
oquvchilar = ["Ali", "Vali", "Sardor", "Malika", "Madina"]

ism = input("Ism kiriting: ")

if ism in oquvchilar:
    print(ism, "ro'yxatda mavjud!")
    print("Birinchi harfi:", ism[0])
else:
    print("O'quvchi ro'yxatda yo'q!")


#T-10
numbers = [12, 5, 8, 17, 20, 3, 10, 7]

for son in numbers:
    if son % 2 == 0:
        print(son, "- Juft son")
    else:
        print(son, "- Toq son")


#T-11
numbers = [2, 5, 8, 11, 14, 17]

for i in range(len(numbers)):
    if numbers[i] < 10:
        numbers[i] = numbers[i] * 2
    else:
        numbers[i] = numbers[i] + 5

print(numbers)


#T-12
products = ["Go'sht", "Non", "Sut", "Tuxum", "Guruch"]
prices = [90000, 4000, 12000, 1800, 15000]

print("===== TOVARLAR DO'KONI =====")
print("1. Go'sht")
print("2. Non")
print("3. Sut")
print("4. Tuxum")
print("5. Guruch")

tanlaw = int(input("Tovarni tanlang: "))

if tanlaw == 1:
    print("Siz Go'shtni tanladingiz.")
    narx = prices[0]
elif tanlaw == 2:
    print("Siz Nonni tanladingiz.")
    narx = prices[1]
elif tanlaw == 3:
    print("Siz Sutni tanladingiz.")
    narx = prices[2]
elif tanlaw == 4:
    print("Siz Tuxumni tanladingiz.")
    narx = prices[3]
elif tanlaw == 5:
    print("Siz Guruchni tanladingiz.")
    narx = prices[4]
else:
    print("Bunday tovar mavjud emas!")
    narx = 0

if narx > 0:
    print("Narxi:", narx, "so'm")
    san = int(input("Qancha kerakligini kiriting: "))
    jami = narx * san
    print("Umumiy summa:", jami, "so'm")
  #T-13
products = ["Non", "Sut", "Go'sht", "Olma", "Banan"]
prices = [4000, 12000, 90000, 8000, 15000]

mahsulot = input("Qanday mahsulot olmoqchisiz? ")

if mahsulot in products:
    index = products.index(mahsulot)
    narx = prices[index]

    soni = int(input("Non qancha kerak? "))

    jami = narx * soni
    print("Umumiy summa:", jami, "so'm")
else:
    print("Bunday mahsulot yo'q!")


#T-14
grades = [
    [5, 4, 3],
    [4, 5, 5],
    [3, 2, 4]
]

# a
for baholar in grades:
    print(baholar)

# b
grades[1][1] = 4

# c
grades[2][0] = 3

# d
print(grades)


#T-15
products = [
    ["Non", 4000, 10],
    ["Sut", 12000, 5],
    ["Go'sht", 90000, 2],
    ["Olma", 8000, 0]
]

for product in products:
    if product[2] >= 5:
        print(product[0], "Sani:", product[2])
        print("Status: Yetkilikli")
    else:
        print(product[0], "Sani:", product[2])
        print("Status: Az qalgan")
