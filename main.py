from datetime import datetime
#
# today = datetime.now()
# print(today)
# tomorrow = datetime.now().timestamp() + 24 * 3600
# tomorrow = datetime.fromtimestamp(tomorrow)
# print(tomorrow > today)
city = input('Alege destinatia')
day = int(input('Alege ziua'))
hour = int(input('Alege ora'))
date = datetime(2024, 12, day, hour)
print(date)
