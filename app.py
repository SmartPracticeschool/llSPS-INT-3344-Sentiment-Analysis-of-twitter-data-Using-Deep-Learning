
from flask import Flask, request, jsonify, render_template
from brain import brain

app = Flask(__name__)
@app.route('/')
def home():
    err = brain(sentiment)
    if err == 0 or err == 1 : err = ''
    return render_template('index.html', result = err)
@app.route('/',methods=['POST'])
def y_predict():
    sentiment = request.form["Message"]
    return render_template('index.html', result = str(brain(sentiment)) + '.png')
if __name__=="__main__":
    app.run()

