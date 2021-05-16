from flask import Flask
import pandas as pd
import ast
from main import RandomImageGenerator
import flask.scaffold

flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
import flask_restful
import sqlite3
from sendEmail import sendEmail
from flask_restful import reqparse
from db_write import email_write

app = Flask(__name__)
api = flask_restful.Api(app)




@app.route('/')
class Generate(flask_restful.Resource):
    def __init__(self):
        self.conn = sqlite3.connect('DB/DB.db')

    def get(self):
        sql = f""" select *  from artpieces where serial_number in (select max(serial_number) from artpieces)"""
        cursor = self.conn.execute(sql)
        return {"data": cursor.fetchall()}

    def post(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('email', required=True)  # add args
        args = parser.parse_args()
        print(args['email'])

        i = RandomImageGenerator()
        output = i.main()

        email_write(output[0], args['email'])

        sendEmail(args['email'], output[1])
        return {"image" : 'sent'}
    pass


api.add_resource(Generate, '/generate')

if __name__ == '__main__':
    app.run()
