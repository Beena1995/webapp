## import libraries for deployment

from flask import Flask, request, jsonify, render_template
import pickle
from pyforest import *
import joblib

## naming our app as app
app = Flask(__name__)

## loading the pickle file for creating web app
model = joblib.load(open("model.pkl", 'rb'))

## defining diff pages of html and specifying features req to be filled in html form

@app.route("/")
def home():
	return render_template("index.html")

## creating a func for pred model by specifying params and feeding to model
@app.route("/predict", methods = ["POST"])
def predict():
	# specifying params as data type float
	int_features = [float(x) for x in requet.form.values()]
	final_features = [np.array(int_features)]
	prediction = model.predict(final_features)
	output = round(prediction[0],2)
	return render_template("index.html", prediction_text = "flower is {}".format(output))

## running the flask app
if __name__=="__main__":
	app.run(debug = True)