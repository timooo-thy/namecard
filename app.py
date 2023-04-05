import flask
from flask import Flask, render_template

app = Flask(__name__)

print(flask.__version__)

@app.route('/')
def run_site():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
