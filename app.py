
from flask import Flask, request, jsonify, render_template
from brain import brain
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html', result = '')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    sentiment = request.form["Message"]
    return render_template('index.html', result = brain(sentiment))
    #return render_template('index.html', result = str(brain(sentiment)) + '.jpg') 
if __name__ == "__main__":
    app.run()
