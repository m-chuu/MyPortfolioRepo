from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
    return "Hello, world!!", 200

@app.route('/getname', methods=["GET"])
def get_name():
    return "Gopi"

@app.route('/name/<name>', methods=["GET"])
def name(name):
    return 'Hello %s' % name

@app.route('/age/<int:age>', methods=["GET"])
def get_age(age):
    return 'Your age is %d' % age, 500  # Using 200 as the status code

@app.route('/static')
def static_method():
    return render_template('static.html')

if __name__ == '__main__':
    app.run(port=5005)

