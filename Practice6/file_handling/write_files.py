#Создаем файл и записываем текст

with open("example.txt", "w", encoding="utf-8") as file:
    file.write("Привет\n")
    file.write("Это Practice 6")