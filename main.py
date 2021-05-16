from random import randrange
from images import Picasso
from db_write import artpiece_write
import sqlite3
from serial import Serial


class RandomImageGenerator:
    def __init__(self):
        self.conn = sqlite3.connect('DB/DB.db')
        self.new_serialNumber = int(Serial(self.conn).new_serialNumber())

    def main(self):
        temp = Picasso(randrange(1, 10), self.new_serialNumber)
        artpiece_write(self.conn, self.new_serialNumber)
        print('Completed!')
        return temp

