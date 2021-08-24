from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np 

model=pickle.load(open("crime_rate.pickle", "rb"))


app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")




@app.route("/result_above_18", methods=["POST"])
def predict_above_18():
    print(request.form)
    initial_features=[int(x) for x in request.form.values()]
    final_features=[np.array(initial_features)]
    print(initial_features)
    print(final_features)
    prediction=model.predict(final_features)
    output=int(prediction[0][0])
    return render_template("firstresult.html", prediction_text="Number of victims in the state: {}".format(output))

@app.route("/result_above_30", methods=["POST","GET"])
def predict_above_30():
    print(request.form)
    initial_features=[int(x) for x in request.form.values()]
    final_features=[np.array(initial_features)]
    print(initial_features)
    print(final_features)
    prediction=model.predict(final_features)
    output=int(prediction[0][1])
    return render_template("secondresult.html", prediction_text="Number of victims in the state: {}".format(output))

@app.route("/result_above_50", methods=["POST","GET"])
def predict_above_50():
    print(request.form)
    initial_features=[int(x) for x in request.form.values()]
    final_features=[np.array(initial_features)]
    print(initial_features)
    print(final_features)
    prediction=model.predict(final_features)
    output=int(prediction[0][2])
    return render_template("thirdresult.html", prediction_text="Number of victims in the state: {}".format(output))

@app.route("/first")
def first():
    return render_template("home.html")

@app.route("/second")
def second():
    return render_template("secondhome.html")

@app.route("/third")
def third():
    return render_template("thirdhome.html")


if __name__=="__main__":
    app.run(debug=True)