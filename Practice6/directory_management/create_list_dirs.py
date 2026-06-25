import os

# Создаем папки
os.makedirs("folder1/folder2", exist_ok=True)

print("Папки созданы")

# Показываем содержимое текущей папки
print(os.listdir())

# Текущая директория
print(os.getcwd())