

#Строка кода которая преобразует заданную строку верблюда в snake case.
import re
text = input("Введите camelCase строку: ")

result = re.sub(r"([A-Z])", r"_\1", text).lower()

print(result)