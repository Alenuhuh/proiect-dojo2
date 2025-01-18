from datetime import datetime
from flights import flights
#
# today = datetime.now()
# print(today)
# tomorrow = datetime.now().timestamp() + 24 * 3600
# tomorrow = datetime.fromtimestamp(tomorrow)
# print(tomorrow > today)
destination = input('Alege destinatia')
month = int(input('Alege luna'))
day = int(input('Alege ziua'))
hour = int(input('Alege ora'))
date = datetime(2025, month, day, hour)
print(date)
x=month
if destination in flights:
    available_flights = flights[destination]
    print(available_flights)

for flights in available_flights
     if x
         return