# Model


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
