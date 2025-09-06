
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

nhanes_data = "nhanes_2015_2016.csv"

df = pd.read_csv(nhanes_data)
print(df.head())

# The aim of this investigation is to identify trends across the NHANES dataset
# I perform an analysis across one variable in this sub-section

# 1. The first analysis is done for education levels for all 5600 participants
# CATEGORICAL SUMMARIES
# Frequency Distribution of variable DMDEDUC2 [Education level]
mode = df.DMDEDUC2.value_counts()
print("Frequency distribution of Education levels:", mode)

import pdb; pdb.set_trace()

# Locate the null (missing) values
null = pd.isnull(df.DMDEDUC2).sum()
print ("Null count of Education levels:", null)

# Replacing the catergocial number with labels by creating a new variable called DMDEDUC2x.
df["DMDEDUC2x"] = df.DMDEDUC2.replace({1: "<9", 2: "9-11", 3: "HS/GED", 4: "Some college/AA", 5: "College", 7: "Refused", 9: "Don't know"})
modex = df.DMDEDUC2x.value_counts()
print("Frequency distribution of Education levels:", modex)

# Replacing gender number with labels by creating a new variable called RIAGENDRx. 
df["RIAGENDRx"] = df.RIAGENDR.replace({1: "Male", 2: "Female"})
genx = df.RIAGENDRx.value_counts()
print("Frequency Distribution of Gender:", genx)

# Proportion
propx = modex / modex.sum()
print("Proportions of Education levels are:", propx)

# NUMERICAL SUMMARIES
# Descriptive statistics
bw = df["BMXWT"].dropna().describe()
print("Discriptive Statistics of Body Weight:", bw)

#Individual statistics 
# Measures of Central Tendency
bwx = df["BMXWT"].dropna()  # Extract all non-missing values of BMXWT into a variable called 'x'
print("Mean Body Weight:", bwx.mean()) # Pandas method
print("Mean Body Weight:", np.mean(bwx)) # Numpy function
print("Median Body Weight:", bwx.median()) 
print("50th percentile Body Weight:", np.percentile(bwx, 50))  # 50th percentile, same as the median
print("75th percentile Body Weight:", np.percentile(bwx, 75))  # 75th percentile
print("Quantile Body Weight:", bwx.quantile(0.75)) # Pandas method for quantiles, equivalent to 75th percentile

# Measures of spread
print("Range of Body Weight:", bwx.max() - bwx.min())
print("SD of BW:", bwx.std())
print("Variance of BW:", bwx.var())

# Eg: calculating the propotion of subjects who are pre-hypertensive based on diastolic blood pressure (between 80 and 89).
dbp = np.mean((df.BPXDI1 >= 80) & (df.BPXDI2 <= 89))
print("Proportion of people with pre-hypertensive DBP:", dbp)

# GRAPHICAL SUMMARIES
# Distribution of Body Weight in Histogram
sns.displot(df.BMXWT.dropna())
plt.show()

# Comparing Systolic and Diastolic blood pressures in first and second measurements. 
bp = sns.boxplot(data=df.loc[:, ["BPXSY1", "BPXSY2", "BPXDI1", "BPXDI2"]])
_ = bp.set_ylabel("Blood pressure in mm/Hg")
plt.show()

# Observing if blood pressure tends to increase with age.
df["agegrp"] = pd.cut(df.RIDAGEYR, [18, 30, 40, 50, 60, 70, 80]) # Create age strata based on these cut points
plt.figure(figsize=(12, 5))  # Make the figure wider than default (12cm wide by 5cm tall)
sns.boxplot(x="agegrp", y="BPXSY1", data=df)  # Make boxplot of BPXSY1 stratified by age group
plt.show() 