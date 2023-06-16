from flask import Flask
import psycopg2
import os

app = Flask(__name__)
hostdb = os.environ['hostdb']
querydb = os.environ['querydb']


@app.route('/')
def hello():
    return 'Hello, Hello!'

@app.route('/ppp')
def aaa():
    return 'ppp page'

@app.route('/add_data')
def huhu():
    con = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host=hostdb,
                                  port="5432",
                                  database="postgres")
    cursor=con.cursor()
    cursor.execute(querydb)
    record = cursor.fetchone()
    return str(record)

if __name__ =='__main__':
    app.run(debug = True, host='0.0.0.0', port='3333')
