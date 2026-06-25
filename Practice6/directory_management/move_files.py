import shutil
import os

os.makedirs("backup", exist_ok=True)

# Перемещаем файл
shutil.move("example.txt", "backup/example.txt")

print("Файл перемещен")