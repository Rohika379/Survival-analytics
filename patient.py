
# pip install lifelines
# import lifelines

import pandas as pd
# Loading the the survival un-employment data
patient = pd.read_csv("C:\\OneDrive\\Desktop\\360digiTMG assignment\\Survival analytics\\Patient.csv")
patient.head()
patient.describe()

from sklearn.preprocessing import LabelEncoder
# creating instance of labelencoder
labelencoder = LabelEncoder()

patient.columns
patient['PatientID']= labelencoder.fit_transform(patient['PatientID'])

patient["PatientID"].describe()

# PatientID is referring to time 
T = patient.PatientID

# Importing the KaplanMeierFitter model to fit the survival analysis
from lifelines import KaplanMeierFitter

# Initiating the KaplanMeierFitter model
kmf = KaplanMeierFitter()

# Fitting KaplanMeierFitter model on Time and Eventtypes for death 
kmf.fit(T, event_observed=patient.Eventtype)

# Time-line estimations plot 
kmf.plot()

# Over Multiple groups 
# For each group, here group is Followup
patient.Followup.value_counts()

# Applying KaplanMeierFitter model on Time and Eventtypes for the group "1"
kmf.fit(T[patient.Followup==1], patient.Eventtype[patient.Followup==1], label='1')
ax = kmf.plot()

# Applying KaplanMeierFitter model on Time and Eventtypes for the group "0"
kmf.fit(T[patient.Followup==0], patient.Eventtype[patient.Followup==0], label='0')
kmf.plot(ax=ax)


