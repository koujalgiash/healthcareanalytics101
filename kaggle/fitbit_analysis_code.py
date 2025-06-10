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

# Verifying number of unique users per dataset
users_in_daily_activity = daily_activity['Id'].nunique()
users_in_daily_sleep = daily_sleep['Id'].nunique()
users_in_hourly_steps = hourly_steps['Id'].nunique()

print("Number of users in daily activity is:", users_in_daily_activity)
print("Number of users in daily sleep is:", users_in_daily_sleep)
print("Number of users in hourly steps is:", users_in_hourly_steps)
print()

# Duplicates
print("Number of duplicates in daily activity is:", daily_activity.duplicated().sum())
print("Number of duplicates in daily sleep is:", daily_sleep.duplicated().sum())
print("Number of duplicates in hourly steps is:", hourly_steps.duplicated().sum())

# Remove duplicates and N/A
daily_activity.drop_duplicates(inplace=True)
daily_sleep.drop_duplicates(inplace=True)
hourly_steps.drop_duplicates(inplace=True)

print("Number of duplicates in daily activity is:", daily_activity.duplicated().sum())
print("Number of duplicates in daily sleep is:", daily_sleep.duplicated().sum())
print("Number of duplicates in hourly steps is:", hourly_steps.duplicated().sum())
