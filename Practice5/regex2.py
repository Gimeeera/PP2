import re

#Строка которая совпадает со строкой, с которой следуют два или три
text = input("Введите строку: ")

if re.fullmatch(r"ab{2,3}", text):
    print("Подходит")
else:
    print("Не подходит")