# Разница между датами в секундах
from datetime import datetime

date1_str = input("Введите первую дату и время (ГГГГ-ММ-ДД ЧЧ:ММ:СС): ")
date2_str = input("Введите вторую дату и время (ГГГГ-ММ-ДД ЧЧ:ММ:СС): ")

date1 = datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")

difference = date2 - date1

print("Разница в секундах:", difference.total_seconds())