from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'secret_key'

def init_db():
    if not os.path.exists('database.db'):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        
        # Users table
        c.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                role TEXT NOT NULL
            )
        ''')

        # Sample users
        c.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", ('doctor1', 'doc123', 'doctor'))
        c.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", ('patient1', 'pat123', 'patient'))

        # Patient data table
        c.execute('''
            CREATE TABLE IF NOT EXISTS patient_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                gender TEXT,
                weight REAL,
                procedure TEXT,
                procedure_date TEXT,
                allergies TEXT,
                temperature REAL,
                heart_rate INTEGER,
                blood_pressure TEXT,
                respiratory_rate INTEGER,
                notes TEXT
            )
        ''')
        conn.commit()
        conn.close()
        print("Database 'database.db' created and initialized.")
    else:
        print("Database already exists.")

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT role FROM users WHERE username = ? AND password = ?", (username, password))
    user = c.fetchone()
    conn.close()

    if user:
        session['username'] = username
        session['role'] = user[0]
        if user[0] == 'doctor':
            return redirect(url_for('view_patients'))
        else:
            return redirect(url_for('form'))
    else:
        return "Invalid credentials"

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        data = (
            request.form['name'],
            request.form['age'],
            request.form['gender'],
            request.form['weight'],
            request.form['procedure'],
            request.form['procedure_date'],
            request.form['allergies'],
            request.form['temperature'],
            request.form['heart_rate'],
            request.form['blood_pressure'],
            request.form['respiratory_rate'],
            ''
        )

        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('''
            INSERT INTO patient_data (name, age, gender, weight, procedure, procedure_date, allergies, 
            temperature, heart_rate, blood_pressure, respiratory_rate, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', data)
        conn.commit()
        conn.close()
        return redirect(url_for('result'))
    return render_template('patient_form.html')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/view')
def view_patients():
    if session.get('role') == 'doctor':
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM patient_data")
        patients = c.fetchall()
        conn.close()
        return render_template('view_patients.html', patients=patients)
    return "Unauthorized"

@app.route('/notes/<int:patient_id>', methods=['GET', 'POST'])
def notes(patient_id):
    if session.get('role') == 'doctor':
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        if request.method == 'POST':
            note = request.form['notes']
            c.execute("UPDATE patient_data SET notes = ? WHERE id = ?", (note, patient_id))
            conn.commit()
        c.execute("SELECT * FROM patient_data WHERE id = ?", (patient_id,))
        patient = c.fetchone()
        conn.close()
        return render_template('doctor_notes.html', patient=patient)
    return "Unauthorized"

if __name__ == '__main__':
    init_db()
    app.run(debug=True)