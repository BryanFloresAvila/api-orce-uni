from flask  import Flask
from flask import request
from utils import getScores, getInformation

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello"
  
@app.route('/getScores/')
def get_scores():
    codeUNI = request.args.get('code')
    cycle = request.args.get('cycle')
    return (getScores(cycle,codeUNI))
  
@app.route('/getInformation/')
def get_information():
    codeUNI = request.args.get('code')
    return (getInformation(codeUNI))

app.run(host='0.0.0.0', port=81)