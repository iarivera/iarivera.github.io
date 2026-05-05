import os
from flask import Flask, render_template, url_for, send_file

app = Flask(__name__, template_folder="templates")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/portfolio')
def portfolio():
    return render_template("portfolio.html")

@app.route("/download_resume")
def download_resume():
    path = 'static/Rivera,Ivan_Resume.pdf'
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run()