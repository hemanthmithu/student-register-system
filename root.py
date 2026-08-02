from flask import Flask, render_template, request
import sqlite3


app = Flask(__name__)


@app.route('/')
def login():
    return render_template('login.html')



@app.route('/register')
def register():
    return render_template('register.html')



@app.route('/dashboard', methods=['GET','POST'])
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
        """,
        (name, course, semester, suggestion))


        conn.commit()
        conn.close()


        return "Student details submitted successfully!"


    return render_template('dashboard.html')



if __name__ == "__main__":
    app.run(debug=True)