from flask import Flask
import psycopg2

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'
@app.route('/Doraemon')
def world():
    return 'Doraemon page!!!!'
@app.route('/digimon')
def eiei():
    return 'Digimon page!!!!'

@app.route('/add_data')
def huhu():
    con = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="192.168.40.199",
                                  port="5432",
                                  database="postgres")
    cursor=con.cursor()
    cursor.execute('SELECT * from persons;')
    record = cursor.fetchone()
    return str(record)

if __name__ =='__main__':
    app.run(debug = True, host='0.0.0.0', port='3333')
