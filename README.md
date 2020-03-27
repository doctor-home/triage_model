# Model


### Data dimensionality:

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

- Triage level, for now we set 5 levels of severity. 1 least severe, 5 most servere.
