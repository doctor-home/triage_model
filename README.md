# Model

## Build and Run Docker Contrainer
The Docker container can be build with the following command:
```
$ docker image build -t triage_predictor .
```

Finally, you can run the docker container with:
```
$ docker run -p 5000:5000 triage_predictor
```

## Prediction Call to Flask
You can get a prediction from the Triage model, by sending it a JSON in the following format:
``` 
{ 
  "patientID" : ... , #string
  "heart_beat" : ..., #int
  "oxygenation" : ..., #float
  "temperature" : ..., #float
  "breathing_rate" : ..., #int
  "preconditions" : ..., #string (None, Hypertension, Asthma, Arthritis, Cancer)
  "fitness" : ..., #int [1,10]
  "smoker" : ... #bool
}
``` 

``` 
$ curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"patientID" : "111111", "heart_beat" : 50, "oxygenation" : 0.99, "temperature" : 36.5, "breathing_rate" : 18, "preconditions" : "None", "fitness" : 9, "smoker" : false }' \
  http://0.0.0.0:5000/predict
``` 


### Data

Input data:

- Patient - clinician Data:    
    
    + name (str)
    + surname (str)
    + Location (categorical)
    + Patient Unique Id (uuid)
    + Doctor Unique Id (uuid)
    
- When the patient was added to the system:
    
    + Timestamp (timedt)
    
- Medical parameters (not a timepoint, it is a history of values):

    + timepoint
    + oxygenation level (percentage)
    + heart beat (real)
    + patient age (int)
    + pregressed conditions (categorical)
    + temperature (float)
    + number of days the symptoms have started (int)
    + breathing rate (float)

Output data:

- Triage level, for now we set 5 levels of severity. 1 least severe, 5 most severe.
More input from clinicians will be required.
- Confidence (%)

### Model and plan

Assumptions:
- not all the features counts the same (breathing rate or oxygenation and age should be the most relevant),
so we have to weight them before applying the model.
- for each feature we have a collection of time-points. The last time-points are the most important ones in
making a prediction.

Plan:
+ Train a random forest (1) to weight the features
+ Non-linear mixed model or regression to get the trend from the historical data 
(extra weight on latest timepoints).
+ Combine latest timepoint and trend in a single input data.
+ Train another random forest (2) to classify the combined data above and to get a prediction.

Random forest 1 and 2 should be trained on different datasets. 
