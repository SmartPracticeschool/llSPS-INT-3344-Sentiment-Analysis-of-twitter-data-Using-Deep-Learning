
import os
from flask import Flask, request, jsonify, render_template
from brain import brain

app = Flask(__name__)
@app.route('/')
def home():
    err = "Saved Model Doesn't Exist"
    if os.path.isfile('./model.h5'): err = ''
    return render_template('index.html', result = err)
@app.route('/',methods=['POST'])
def y_predict():
    sentiment = request.form["Message"]
    return render_template('index.html', result = str(brain(sentiment)) + '.png')
if __name__=="__main__":
    app.run()

