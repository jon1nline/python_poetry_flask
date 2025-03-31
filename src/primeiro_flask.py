from flask import Flask, url_for, request
app = Flask(__name__)


@app.route('/olamundo/<user>/<int:idade>/<float:altura>')
def hello_world(user,idade,altura):
    return {
        "Usuario": user,
        "Idade":idade,
        "Altura":altura,

    }

@app.route('/bemvindo')
def hello():
    return {"message": "Olá mundo!"}


@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about',methods=['GET','POST','PUT'])
def about():
    if request.method == 'GET':
        return 'This is a GET Method'
    elif request.method == 'POST':
        return 'This is a POST method'
    else:
        return 'This method is not allowed'

with app.test_request_context():
    print(url_for('hello'))
    print(url_for('projects'))
    print(url_for('about', next='/'))
    