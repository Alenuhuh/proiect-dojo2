from bdb import Breakpoint
from datetime import datetime
from flights import flights
#
# today = datetime.now()
# print(today)
# tomorrow = datetime.now().timestamp() + 24 * 3600
# tomorrow = datetime.fromtimestamp(tomorrow)
# print(tomorrow > today)
# destination = input('Alege destinatia')
# month = int(input('Alege luna'))
# day = int(input('Alege ziua'))
# hour = int(input('Alege ora'))
destination = 'Londra'
month = 8
day = 11
hour = 13
budget = 300
date = datetime(2025, month, day, hour)


if destination in flights:
    available_flights = flights[destination]
    # min flight timedelta is 14 days
    time_min = 14*3600*24
    chosen_flight = None
    for flight in available_flights:
        diff = (flight['date'] - date).total_seconds()
        if diff < time_min and diff > 0 and budget >= flight['pret']:
            chosen_flight = flight
            time_min = diff
    print(chosen_flight)
    if chosen_flight is None:
        print('Nu avem zbor disponibil')
    else:
        flight_date = chosen_flight['date']
        print(f'Urmatorul zbor este in luna: {flight_date.month}, ziua: {flight_date.day}, la ora: {flight_date.hour}, costa {chosen_flight['pret']}')
