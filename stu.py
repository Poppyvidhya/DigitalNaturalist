from flask import Flask, render_template
import sqlite3
app = Flask(__name__)
@app.route('/')
def index():
    conn = sqlite3.connect('your_database.db')  # Replace 'your_database.db' with your database file path
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM your_table')  # Replace 'your_table' with your table name
    data = cursor.fetchall()
    conn.close()
    return render_template('study.html', data=data)
