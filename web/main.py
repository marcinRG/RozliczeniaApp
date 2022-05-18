from flask import Flask

app = Flask(__name__)


@app.route('/login')
def login():
    pass




if __name__ == '__main__':
    app.run(debug=True)
