from flask import Flask, render_template
import database

app = Flask(__name__)
database.create_db()

@app.route('/')
def index():
    ads = database.read_ad()
    return render_template('index.html', ads=ads)

app.run()
