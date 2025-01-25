from flask import Flask, render_template, request, redirect, url_for
import database as db

app = Flask(__name__)
db.init_db()

@app.route("/")
def index():
    ads = db.get_ads()
    return render_template("index.html", ads=ads)

@app.route("/create", methods=["POST"])
def create():
    title = request.form.get("title")
    content = request.form.get("content")
    if title and content:
        db.create_ad(title, content)
    return redirect(url_for("index"))

@app.route("/update/<int:ad_id>", methods=["POST"])
def update(ad_id):
    title = request.form.get("title")
    content = request.form.get("content")
    if title and content:
        db.update_ad(ad_id, title, content)
    return redirect(url_for("index"))

@app.route("/delete/<int:ad_id>")
def delete(ad_id):
    db.delete_ad(ad_id)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
