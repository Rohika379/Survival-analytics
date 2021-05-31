# Survival Analysis in R

install.packages('survminer')
install.packages("survival")

library(survminer)
library(survival)

??survminer
??survival
library(readxl)
ecg <-read_excel(file.choose())

sum(is.na(ecg))
ecg <-na.omit(ecg)

attach(ecg)
str(ecg)

# Define variables 
time <- survival_time_hr
event <- alive
group <- group

# Descriptive statistics
summary(time)
table(event)
table(group)

# Kaplan-Meier non-parametric analysis
kmsurvival <- survfit(Surv(time, event) ~ 1)

summary(kmsurvival)

plot(kmsurvival, xlab="Time", ylab="Survival Probability")

ggsurvplot(kmsurvival, data=ecg, risk.table = TRUE)


# Kaplan-Meier non-parametric analysis by group
kmsurvival1 <- survfit(Surv(time, event) ~ group)
summary(kmsurvival1)

plot(kmsurvival1, xlab="Time", ylab="Survival Probability")
ggsurvplot(kmsurvival1, data=ecg, risk.table = TRUE)

###############
