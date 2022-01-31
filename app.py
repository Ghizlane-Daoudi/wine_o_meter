from typing import List
import joblib
from flask import Flask, request, json, jsonify, render_template
from werkzeug.exceptions import HTTPException

MODEL_PATH = "models/model.joblib"

app = Flask(__name__)


def make_prediction(input: List[List]):
    """Return a prediction with our regression model.
    """
    # Load model
    regressor = joblib.load(MODEL_PATH)
    # Make prediction (the regressor expects a 2D array that is why we put year
    # in a list of list) and return it
    prediction = regressor.predict(input)
    print(prediction)
    return prediction


@app.route("/predict", methods=["POST"])
def predict():
    # Get JSON as dictionnary
    json_input = request.get_json()
    prediction = make_prediction(list(json_input["input"]))
    response = {
        "prediction": str(prediction),
    }
    return jsonify(response), 200


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
