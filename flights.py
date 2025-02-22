from datetime import datetime

class Flight:
    def __init__(self, datetime, pret):
        self.date = datetime
        self.pret = pret

    def __str__(self):
        return f'Zbor in data de {self.date} cu pretul de {self.pret}'


'''
    string : [{ data: datetime, pret:number  }]
'''
flights ={
   'Timisoara':[Flight(datetime(2025, 11, 2, 16), 200),
                Flight(datetime(2025, 9, 30, 11) , 200),
                Flight(datetime(2025, 7, 12, 19),  230),
                Flight(datetime(2025, 6, 5, 23), 210),
                Flight(datetime(2025, 4, 27, 4), 250),
                Flight(datetime(2025, 3, 20, 13) , 280)],

    'Londra':[Flight( datetime(2025, 8, 18, 20) , 350),
              Flight( datetime(2025, 8, 11, 5) , 360),
              Flight( datetime(2025, 6, 6, 22) , 355),
              Flight( datetime(2025, 3, 25, 10) , 380),
              Flight( datetime(2025, 2, 28, 17) , 350)],

    'Seol':[Flight(datetime(2025, 12, 2, 16) ,450),
            Flight(datetime(2025, 10, 14, 11) , 500),
            Flight(datetime(2025, 6, 29, 9) , 550),
            Flight(datetime(2025, 2, 17, 19) ,  530)],

    'New York':[Flight(datetime(2025, 12, 14, 8) ,  400),
                Flight(datetime(2025, 11, 30, 18) , 450),
                Flight(datetime(2025, 6, 15, 23) ,  440),
                Flight(datetime(2025, 4, 20, 18) ,  420),
                Flight(datetime(2025, 1, 10, 6) , 450)],

    'Las Vegas':[Flight(datetime(2025, 11, 15, 3) ,600),
                 Flight(datetime(2025, 8, 2, 18) , 610),
                 Flight(datetime(2025, 5, 14, 13) ,  600),
                 Flight(datetime(2025, 2, 27, 8) , 630)],

    'Singapore':[Flight(datetime(2025, 11, 7, 12) ,300),
                 Flight(datetime(2025, 9, 1, 3) , 400),
                 Flight(datetime(2025, 4, 18, 14), 350),
                 Flight(datetime(2025, 2, 15, 20) ,325)],

    'Tokyo':[Flight(datetime(2025, 12, 26, 18) ,  500),
             Flight(datetime(2025, 10, 14, 14) ,  660),
             Flight(datetime(2025, 7, 28, 21) , 850),
             Flight(datetime(2025, 5, 21, 4) , 750),
             Flight(datetime(2025, 3, 19, 19) , 650)]
}
