import re
import json

# Читаем чек
with open("raw.txt", "r", encoding="utf-8") as file:
    text = file.read()

#Извлекает названия товаров
products = re.findall(r"\d+\.\n(.*?)\n\d+,\d+\s+x", text)

#Извлекает стоимости товаров
prices = re.findall(r"Стоимость\n([\d\s]+,\d+)", text)

#Переводит цены в числа
price_numbers = []

for price in prices:
    clean_price = price.replace(" ", "").replace(",", ".")
    price_numbers.append(float(clean_price))

#Считает сумму
total = sum(price_numbers)

#Ищет дату и время
datetime_match = re.search(
    r"Время:\s*(\d{2}\.\d{2}\.\d{4}\s+\d{2}:\d{2}:\d{2})",
    text
)

datetime_value = datetime_match.group(1)

#Ищет способ оплаты
payment_match = re.search(
    r"(Банковская карта|Наличные)",
    text
)

payment_method = payment_match.group(1)

#Формирует словарь
receipt = {
    "products": products,
    "prices": price_numbers,
    "total": total,
    "datetime": datetime_value,
    "payment_method": payment_method
}

print(json.dumps(receipt, indent=4, ensure_ascii=False))