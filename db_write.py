from images import serial_name_pair
from datetime import datetime
import random
import yaml
import sqlite3

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
stream = open("config.yaml", 'r')
config = yaml.load(stream, Loader=yaml.FullLoader)


def make_uuid():
    return ''.join([random.choice('0123456789ABCDEF') for j in range(20)])


def artpiece_write(conn, new_serialNumber):
    sql = f"""INSERT INTO artpieces (UUID,serial_number,datestr,Author,Content) \
            VALUES ("%s",%d,"%s","%s","%s") """ % (serial_name_pair[new_serialNumber], new_serialNumber, dt_string,
                                                   serial_name_pair['author'], serial_name_pair['content'])
    conn.execute(sql)
    conn.commit()
    return serial_name_pair[new_serialNumber]


def email_write(im, email):
    sql = f""" INSERT INTO email (UUID, email, artpiece, datestr) \
            VALUES ("%s","%s","%s","%s") """ % (make_uuid(), email, im, dt_string)

    conn = sqlite3.connect(config["product"]["email_DB"])
    conn.execute(sql)
    conn.commit()