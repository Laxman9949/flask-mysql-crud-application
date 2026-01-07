from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",   # add password if exists
    database="flaskcrud"
)

cursor = db.cursor()

@app.route('/')
def index():
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    return render_template('index.html', users=data)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    email = request.form['email']
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    db.commit()
    return redirect('/')
@app.route('/update', methods=['POST'])
def update():
    id = request.form['id']
    name = request.form['name']
    email = request.form['email']

    cursor.execute(
        "UPDATE users SET name=%s, email=%s WHERE id=%s",
        (name, email, id)
    )
    db.commit()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    cursor.execute("DELETE FROM users WHERE id=%s", (id,))
    db.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
