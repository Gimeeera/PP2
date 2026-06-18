# Выводим вчера, сегодня и завтра

from datetime import datetime, timedelta

today = datetime.today()

yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)