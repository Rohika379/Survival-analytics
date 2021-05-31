# Survival Analysis in R

install.packages('survminer')
install.packages("survival")

library(survminer)
library(survival)

??survminer
??survival

patient <- read.csv("C:\\Users\\Desktop\\360digiTMG assignment\\Survival analytics\\Patient.csv")
patient$PatientID <-factor(patient$PatientID)

patient$PatientID <-as.numeric(patient$PatientID)
attach(patient)
str(patient)

# Define variables 
time <- PatientID
event <- Eventtype
group <- Followup
# Descriptive statistics
summary(time)
table(event)
table(group)

# Kaplan-Meier non-parametric analysis
kmsurvival <- survfit(Surv(time, event) ~ 1)

summary(kmsurvival)

plot(kmsurvival, xlab="Time", ylab="Survival Probability")

ggsurvplot(kmsurvival, data=patient, risk.table = TRUE)


# Kaplan-Meier non-parametric analysis by group
kmsurvival1 <- survfit(Surv(time, event) ~ group)
summary(kmsurvival1)

plot(kmsurvival1, xlab="Time", ylab="Survival Probability")
ggsurvplot(kmsurvival1, data=patient, risk.table = TRUE)

###############
