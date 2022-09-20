import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
import pandas as pd

df = pd.read_csv("2655021.csv")

format = '%Y-%m-%d'
df['Datetime'] = pd.to_datetime(df['DATE'], format = format)
df = df.set_index(pd.DatetimeIndex(df['Datetime']))

plt.figure(figsize = (12., 6.))

plt.plot(df['Datetime'], df['TMAX'], color = "#CE0809", label = r"$Daily T_{max}$")
plt.plot(df['Datetime'], df['TMIN'], color = "#308AE4", label = r"$Daily T_{min}$")

plt.xlabel("Date")
plt.ylabel("Temperature")

plt.legend(loc = "lower right")
plt.grid()
plt.autoscale(enable = True, axis = 'x', tight = True)

plt.show()

count = 0

start_date = '01-01-1900'
end_date = '12-31-1909'

values = (df['Datetime'] >= start_date) & (df['Datetime'] <= end_date)
new_df = df.loc[values]
bool_df = (new_df['TMAX'] >= 30.0)

for i in range(len(bool_df)):
    if bool_df[i] == True:
        count += 1

print("The number of days with a maximum temperature greater than or equal to 30.0 C is " + str(count) + ".")

count = 0

start_date = '01-01-2010'
end_date = '12-31-2020'

values = (df['Datetime'] >= start_date) & (df['Datetime'] <= end_date)
new_df = df.loc[values]
bool_df = (new_df['TMAX'] >= 30.0)

for i in range(len(bool_df)):
    if bool_df[i] == True:
        count += 1

print("The number of days with a maximum temperature greater than or equal to 30.0 C is " + str(count) + ".")