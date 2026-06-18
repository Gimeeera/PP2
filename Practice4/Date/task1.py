# Вычитаем 5 дней

from datetime import datetime, timedelta

today = datetime.today()

new_date = today - timedelta(days=5)

print(new_date)