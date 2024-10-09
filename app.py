import flask
from flask import Flask
from flask import Flask, render_template
# from mongo import cluster

app = Flask(__name__)



@app.route('/products')
def products():
    return render_template('index.html')

# @app.route('')
# def name():
#     pass

if __name__ == "__main__":
    app.run(debug=True)