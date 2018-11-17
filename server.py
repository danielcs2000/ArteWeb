from flask import Flask, render_template, request, session, Response
from database import connector
from model import entities
import json
db = connector.Manager()
engine = db.createEngine()
primo = 73939133

app = Flask(__name__)
app.secret_key = 'Security Key'  # SECURITY KEY

cache = {}

@app.route('/')
def index():
    return render_template('productos.html')
# FIN

if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, debug=True, host=('localhost'))
