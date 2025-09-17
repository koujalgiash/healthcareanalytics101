
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

nhanes_data = "/Users/aishwaryarkoujalgi/Docs/Coding Exercises/healthcareanalytics101/NHANES_Trends/nhanes_2015_2016.csv"
df = pd.read_csv(nhanes_data)
print(df.head())

############ PART 1: Understanding and Visualizing Data ############

# 1. CATEGORICAL SUMMARIES
# Frequency Distribution of variable DMDEDUC2 [Education level]
mode = df.DMDEDUC2.value_counts()
print("Frequency distribution of Education levels:", mode)

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

# 2. NUMERICAL SUMMARIES
# Descriptive statistics
bw = df["BMXWT"].dropna().describe()
print("Discriptive Statistics of Body Weight:", bw)

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

# 3. GRAPHICAL SUMMARIES
# Distribution of Body Weight in Histogram
ax = sns.histplot(df.BMXWT.dropna())
ax.set(title="Distribution of Body Weight", xlabel="Body Weight (kg)", ylabel="Count")
plt.show()

# Side-by-side Boxplot 
# Comparing Systolic and Diastolic blood pressures in first and second measurements. 
bp_cols = {
    "BPXSY1": "Systolic BP 1",
    "BPXSY2": "Systolic BP 2",
    "BPXDI1": "Diastolic BP 1",
    "BPXDI2": "Diastolic BP 2"
}
bp = sns.boxplot(data=df.loc[:, bp_cols.keys()].rename(columns=bp_cols))
bp.set(title= "Comparing SBP and DBP in two measurements", xlabel= "Measurements", ylabel= "Blood pressure in mm/Hg")
plt.show()

# Side-by-side Boxplot with stratification
# Observing blood pressure trends with age. 
df["agegrp"] = pd.cut(df.RIDAGEYR, [18, 30, 40, 50, 60, 70, 80]) # Create age groups
bp_first = {
    "BPXSY1": "Systolic BP 1",
    "BPXDI1": "Diastolic BP 1"
}
plt.figure(figsize=(12, 5))
bp_1= sns.boxplot(
    x="agegrp",
    y="BP_Value",
    hue="BP_Type",
    data=df.melt(id_vars="agegrp", value_vars=bp_first.keys(),
                 var_name="BP_Type", value_name="BP_Value").replace({"BP_Type": bp_first})
)
bp_1.set(title= "Trends in Systolic Blood Pressure with Age", xlabel= "Age Group", ylabel= "Blood pressure in mm/Hg")
plt.show() 


############ PART 2: Inferential Statistical Analysis ############


