
# pip install lifelines
# import lifelines

import pandas as pd
# Loading the the survival un-employment data
ecg = pd.read_excel(r"C:/Users/Desktop/360digiTMG assignment/Survival analytics/ECG_Surv.xlsx" )
ecg=ecg.iloc[:,[0,1,11]]
ecg=ecg.rename(columns={'survival_time_hr':'time'})

ecg.head()
ecg.describe()

ecg["time"].describe()

# time is referring to time 
T = ecg.time

# Importing the KaplanMeierFitter model to fit the survival analysis
from lifelines import KaplanMeierFitter

# Initiating the KaplanMeierFitter model
kmf = KaplanMeierFitter()

# Fitting KaplanMeierFitter model on Time and alives for death 
kmf.fit(T, event_observed=ecg.alive)

# Time-line estimations plot 
kmf.plot()

# Over Multiple groups 
# For each group, here group is group
ecg.group.value_counts()

# Applying KaplanMeierFitter model on Time and alives for the group "1"
kmf.fit(T[ecg.group==1], ecg.alive[ecg.group==1], label='1')
ax = kmf.plot()

# Applying KaplanMeierFitter model on Time and alives for the group "0"
kmf.fit(T[ecg.group==0], ecg.alive[ecg.group==0], label='0')
kmf.plot(ax=ax)


