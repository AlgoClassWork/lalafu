from flask import Flask, render_template, request, redirect, url_for
import database

app = Flask(__name__)
database.create_db()

@app.route('/')
def index():
    ads = database.read_ad()
    return render_template('index.html', ads=ads)

@app.route('/create', methods=['POST'])
def create():
    title = request.form.get('title')
    content = request.form.get('content')
    database.create_ad(title, content)
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    title = request.form.get('title')
    content = request.form.get('content')
    database.update_ad(id, title, content)
    return redirect(url_for('index'))

app.run()
