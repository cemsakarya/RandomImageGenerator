class Serial:
    def __init__(self, conn):
        self.conn = conn

    def last_serial_number(self):
        sql = f""" select max(serial_number) from artpieces """
        cursor = self.conn.execute(sql)
        return int([int(i[0]) for i in cursor.fetchall()][0])

    def new_serialNumber(self):
        sql = f""" select max(serial_number) from artpieces """
        cursor = self.conn.execute(sql)
        return int([int(i[0]) for i in cursor.fetchall()][0]) + 1