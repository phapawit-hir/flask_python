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
def eiei():
    con = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")
    con.cursor().execute('SELECT * from persons;')
    record = cursor.fetchone()
    return record

if __name__ =='__main__':
    app.run(debug = True, host='0.0.0.0', port='3333')
