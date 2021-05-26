from flask import Flask, render_template, request
import pickle
import numpy as np

app=Flask(__name__)
model=pickle.load(open("model.pickle","rb"))

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/",methods=["POST"])
def predict():
    values=[["gender",0],["age",0],["hypertension",0],["heartdisease",0],["residence",0],["glucose",0],["bmi",0],["formellysmoked",0],["neversmoked",0],["smokes",0],["unknown",0]]
    form_keys=request.form
    print(form_keys)
    features=[]
    for i in values:
        if(i[0] in form_keys):
            features.append(form_keys[i[0]])
        else:
            features.append(i[1])
 #   features = [int(x) for x in request.form.values()]
#    print("This is request",features)
    values = [np.array(features)]
    prediction = model.predict(values)
    if(prediction==1):
        return render_template("home.html",prediction_text="There are changes of stroke.")
    return render_template("home.html",prediction_text="There are no chances of stroke.")
if __name__=="__main__":
    app.run(debug=True)