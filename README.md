# Model


### Data

Input data: as provided by ![data_generator](https://github.com/doctor-home/data_simulator) for now in its internal folder.

### Model and plan

Assumptions:
- not all the features counts the same (breathing rate or oxygenation and age should be the most relevant),
so we have to weight them before applying the model.
- for each feature we have a collection of time-points. The last time-points are the most important ones in
making a prediction.

Plan:
+ Train a random forest (1) to weight the features (expecting age and breathing rate more relevant).
+ Non-linear mixed model or regression to get the trend from the historical data 
(extra weight on latest timepoints).
+ Combine latest timepoint and trend in a single input data.
+ Train another random forest (2) to classify the combined data above and to get a prediction.

Warning: do make sure the training data are balanced.