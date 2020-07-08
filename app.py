
from flask import Flask, request, jsonify, render_template

#from brain import brain


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    sentiment = request.form["Message"]
    
    #prediction = model.predict(x_test)
    #print(prediction)
    #output=prediction[0][0]
    #return render_template('index.html', 
  #prediction_text=
  #'Compressive Strength of Concrete kg/m^3 {}'.format(output))
    return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True)
