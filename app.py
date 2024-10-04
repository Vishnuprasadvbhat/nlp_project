import flask
from flask import Flask
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/hello')
def hello():
    return render_template('home.html')


@app.route('/products')
def products():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)