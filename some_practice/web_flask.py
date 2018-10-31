from flask import lask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
  return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def sigin_form():
  return '''<form action="/signin" method="post"
              <p><input name="username"></p> 
              <p><button type="submit">Sigin</button></p> 
            </form>'''