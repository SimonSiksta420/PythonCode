import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uvod')
def uvod():
    return render_template('uvod.html')

@app.route('/book')
def book():
    return render_template('book.html')

@app.route('/woman')
def woman():
    return render_template('woman.html')

@app.route('/man')
def man():
    return render_template('man.html')

@app.route('/presidential_form')
def presidential_form():
    return render_template('presidential_form.html')

@app.route('/test/<repo>/<namo>')
def test(repo, namo):
    return render_template('test.html', repo=int(repo), namo=namo)

@app.route('/jmenovani/<jmeno>')
def jmenovani(jmeno):
    return render_template('jmenovani.html', jmeno=jmeno)

@app.route('/database', methods=['GET', 'POST'])
def database():
    if request.method == 'POST':
        # Insert data into the database
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']
        conn = sqlite3.connect('example.db')
        conn.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", (name, email, age))
        conn.commit()
        conn.close()
        # Redirect to the same page to display the updated data
        return redirect(url_for('database'))
    else:
        # Check if a search query was submitted
        search_query = request.args.get('q', '')
        conn = sqlite3.connect('example.db')
        if search_query:
            # If a search query was submitted, retrieve only the matching rows from the database
            cursor = conn.execute("SELECT * FROM users WHERE name LIKE ? OR email LIKE ?", ('%{}%'.format(search_query), '%{}%'.format(search_query)))
        else:
            # If no search query was submitted, retrieve all the rows from the database
            cursor = conn.execute("SELECT * FROM users")
        users = [dict(id=row[0], name=row[1], email=row[2], age=row[3]) for row in cursor.fetchall()]
        conn.close()
        return render_template('database.html', users=users, search_query=search_query)

if __name__ == '__main__':
    app.run()