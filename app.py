"""
Backend script to give predictions and train triage detection of patient data
part of CodeVsCovid19 Hackathon

Author: Claudio Fanconi
Email: claudio.fanconi@outlook.com
"""

# Import libraries
from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

app = Flask(__name__)

# Broadcast
HOSTNAME = "0.0.0.0"
# HTTP Port
PORT = 5000
FILENAME = "finalized_model.sav"

print("Loading Classifier from Disk...")
# load the model from disk
model = pickle.load(open(FILENAME, "rb"))
print("Done.\n")


# root
@app.route("/")
def index():
    """
    this is a root dir of my server
    return:
        str where the user is greeted
    """
    return "hello there %s" % request.remote_addr


# POST
@app.route("/predict", methods=["POST"])
def predict():
    """
    Predicts the Triage level of patient.
    return:
        json response containing the prediciton
    """

    json = request.get_json()

    patientID = str(json["patientID"])
    preconditions = str(json["preconditions"])

    if preconditions == "Arthritis":
        json["preconditions_Arthritis"] = 1
        json["preconditions_Asthma"] = 0
        json["preconditions_Cancer"] = 0
        json["preconditions_Hypertension"] = 0
        json["preconditions_None"] = 0

    elif preconditions == "Asthma":
        json["preconditions_Arthritis"] = 0
        json["preconditions_Asthma"] = 1
        json["preconditions_Cancer"] = 0
        json["preconditions_Hypertension"] = 0
        json["preconditions_None"] = 0

    elif preconditions == "Cancer":
        json["preconditions_Arthritis"] = 0
        json["preconditions_Asthma"] = 0
        json["preconditions_Cancer"] = 1
        json["preconditions_Hypertension"] = 0
        json["preconditions_None"] = 0

    elif preconditions == "Hypertension":
        json["preconditions_Arthritis"] = 0
        json["preconditions_Asthma"] = 0
        json["preconditions_Cancer"] = 0
        json["preconditions_Hypertension"] = 1
        json["preconditions_None"] = 0

    else:
        json["preconditions_Arthritis"] = 0
        json["preconditions_Asthma"] = 0
        json["preconditions_Cancer"] = 0
        json["preconditions_Hypertension"] = 0
        json["preconditions_None"] = 1

    del json["preconditions"]
    X = pd.DataFrame(json, index=[0])
    X = X.drop(["patientID"], axis=1)

    # Predict Model
    try:
        y_pred = model.predict(X)
        y_proba = model.predict_proba(X)

    except:
        response = {"STATUS": "FAILED", "ERROR": "Something went wrong..."}
        return jsonify(response)

    # Build response:
    response = {
        "STATUS": "OK",
        "patientID": patientID,
        "triage_level": int(y_pred[0]),
        "PROBABILITY": y_proba.max(),
    }
    return jsonify(response)


if __name__ == "__main__":
    app.run(host=HOSTNAME, port=PORT)
