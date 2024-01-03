from time import sleep
from datetime import datetime
from os import system
import random

WORK_DIR = '/home/jsplinter/Documents/Kerstdorp/'
XMAS_LIST = ['ChrismasJingle', 'HoHoHoMerryXmas', 'InstrumentsWeWishYouAMerryXmas', 'MessageFromSanta', 'MusicboxCarolSound']
PARTY_LIST = [12-25, 12-26]

class KerstdorpSound:
    def __init__(self):
        self.random_minutes_list = []

    def check_datetime(self):
        '''Bepaald de aantal minuten van actuele tijd'''

        self.hours = datetime.today().hour
        self.minutes = datetime.today().minute
        self.month_day = f'{datetime.today().month}-{datetime.today().day}'

    def random_list(self):
        ''''Kiest een willekeurig getal middels bepaalde formule'''
        self.random_minutes_list = []

        def random_minutes():
            return random.choice([minute for minute in range(5,55) if not 25 <= minute <= 35])

        # Maak een random minutenlijst aan voor kerstdagen
        for x in range(2):
            self.random_minutes_list.append(random_minutes())

    def which_sound(self):
        '''Bepaal welke muziekstuk afgespeeld dient te worden'''
        self.check_datetime()

        xmas = True if self.month_day in PARTY_LIST else False

        if self.minutes == 0:
            self.random_list() if xmas else None
            system(f'aplay -D hw:2,0 {WORK_DIR}BigBen/hourlychimebeg.wav')
            system(f'aplay -D hw:2,0 {WORK_DIR}BigBen/bigbenstrikes{self.hours}.wav')

        elif self.minutes == 30 and self.month_day != '1-1':
            system(f'aplay -D hw:2,0 {WORK_DIR}BigBen/hourlychimebeg.wav')

        elif self.minutes == 30 and self.month_day == '1-1':
            system(f'aplay -D hw:2,0 {WORK_DIR}NewYear/happynewyear.wav')

        elif self.minutes in self.random_minutes_list:
            xmas_number = randint(0, 4)
            system(f'aplay -D hw:2,0 {WORK_DIR}Xmas/{XMAS_LIST[xmas_number]}.wav')
    
        sleep (61)


def main():
    print('Kerstdorp py is geladen')
    app = KerstdorpSound()

    while True:
        app.which_sound()


if __name__ == '__main__':
    main()
