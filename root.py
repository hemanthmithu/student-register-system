from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = "mysecretkey"

ADMIN_USERNAME = "mithun"
ADMIN_PASSWORD = "5599"


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():

    if request.method == "POST":

        name = request.form['name']
        course = request.form['course']
        semester = request.form['semester']
        suggestion = request.form['suggestion']

        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO students(name, course, semester, suggestion)
        VALUES (?, ?, ?, ?)
        """, (name, course, semester, suggestion))

        conn.commit()
        conn.close()

        return "Student details submitted successfully!"

    return render_template('dashboard.html')


@app.route('/admin', methods=['GET', 'POST'])
def admin():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin'] = True
            return redirect(url_for('view'))

        return "Invalid Username or Password"

    return render_template('admin.html')


@app.route('/view')
def view():

    if not session.get('admin'):
        return redirect(url_for('admin'))

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    conn.close()

    return render_template("view.html", records=records)


@app.route('/logout')
def logout():
    session.pop('admin', None)
    return redirect(url_for('admin'))


if __name__ == "__main__":
    app.run(debug=True)