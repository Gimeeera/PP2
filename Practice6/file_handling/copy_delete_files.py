import shutil
import os

# Копируем файл
shutil.copy("example.txt", "backup.txt")

print("Файл скопирован")

#Скопированный файл и ее вывод
with open("backup.txt", "r", encoding="utf-8") as file:
    text = file.read()
print(text)


# Удаляем копию
os.remove("backup.txt")

print("Файл удален")