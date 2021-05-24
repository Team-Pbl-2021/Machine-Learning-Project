from flask import Flask, render_template
import pickle
import numpy as np

app=Flask(__name__)
model=pickle.load(open("model.pkl","rb"))

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/",methods=["POST"])
def predict():
    features = [int(x) for x in request.form.values()]
    print("This is request",features)
    values = [np.array(features)]
    prediction = model.predict(values)
    return_value = round(prediction[0], 2)
    return render_template("home.html",prediction_text="There are changes of stroke if value is 1 : {}".format(return_value))

if __name__=="__main__":
    app.run(debug=True)