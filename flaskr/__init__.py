import os

from flask import Flask, render_template

app = Flask(__name__, template_folder="./pages")

@app.route('/')
def index():
    return render_template("index.html")

def portfolio_page(path):
    return render_template("portfolio.html")

if __name__ == '__main__':
    app.run()