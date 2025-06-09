import pandas as pd
from utils import CSV_DAILY_ACTIVITY_MERGED, CSV_DAILY_SLEEP, CSV_HOURLY_STEPS

''' TRIAL CODE- 

# To read a dataset (daily activity merged) into a dataframe
df= pd.read_csv(CSV_DAILY_ACTIVITY_MERGED)
#print(df)

# Exploratory data analyis on dataframe
df.shape 
df.columns
df.info()
print(df.describe())
df.head()
df.tail()
print(df.isnull().sum())
print(df.duplicated().sum())

'''

# Preview datasets
daily_activity = pd.read_csv(CSV_DAILY_ACTIVITY_MERGED)
daily_sleep = pd.read_csv(CSV_DAILY_SLEEP)
hourly_steps = pd.read_csv(CSV_HOURLY_STEPS)

#print(daily_activity)
#print(daily_sleep)
#print(hourly_steps)

print(daily_activity.describe())
print(daily_sleep.describe())
print(hourly_steps.describe())
