
from flask import Flask, request, jsonify, render_template
# from brain import brain
import random
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/y_predict',methods=['POST'])
def y_predict():
    sentiment = request.form["Message"]
    return render_template('index.html',result=random.randint(0,1))
if __name__=="__main__":
    app.run()

