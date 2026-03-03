import pandas as pd
import matplotlib.pyplot as plt
from calendar import month_abbr

df = pd.read_csv('fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv')

#transform the Data_Value column
df["Date"] = pd.to_datetime(df["Date"])

# Convert to C
df["Data_Value"] /= 10

# Seperate max from min
df_max = df[df["Element"] == 'TMAX']
df_min = df[df["Element"] == 'TMIN']

# create a DataFrame of maximum temperature by date
df_max = df_max[~((df_max['Date'].dt.month == 2) & (df_max['Date'].dt.day == 29))].groupby("Date")["Data_Value"].max().reset_index()

# create a DataFrame of minimum temperatures by date
df_min = df_min[~((df_min['Date'].dt.month == 2) & (df_min['Date'].dt.day == 29))].groupby("Date")["Data_Value"].min().reset_index()

cutoff = pd.Timestamp("2015-1-1")

# calculate the minimum and maximum values for the day of the year for 2005 through 2014
df_max["Month"] = df_max["Date"].dt.month
df_min["Month"] = df_min["Date"].dt.month
df_max["Day"] = df_max["Date"].dt.day
df_min["Day"] = df_min["Date"].dt.day

df_05_14_max = df_max[df_max["Date"] < cutoff].groupby([df_max["Month"], df_max["Day"]])["Data_Value"].max().reset_index()
df_05_14_min = df_min[df_min["Date"] < cutoff].groupby([df_min["Month"], df_min["Day"]])["Data_Value"].min().reset_index()

# calculate the minimum and maximum values for the years 2015
df_15_max = df_max[df_max["Date"] >= cutoff].groupby([df_max["Month"], df_max["Day"]])["Data_Value"].max().reset_index()
df_15_min = df_min[df_min["Date"] >= cutoff].groupby([df_min["Month"], df_min["Day"]])["Data_Value"].min().reset_index()

plt.figure(figsize=(30, 15))

# Align indices for comparison
df_05_14_max = df_05_14_max.sort_values(by=["Month", "Day"]).reset_index(drop=True)
df_05_14_min = df_05_14_min.sort_values(by=["Month", "Day"]).reset_index(drop=True)
df_15_max = df_15_max.sort_values(by=["Month", "Day"]).reset_index(drop=True)
df_15_min = df_15_min.sort_values(by=["Month", "Day"]).reset_index(drop=True)

# Plot max and min temperatures for 2005-2014
plt.plot(df_05_14_max["Data_Value"], color="salmon", label="2005-2014 Max Temp")
plt.plot(df_05_14_min["Data_Value"], color="steelblue", label="2005-2014 Min Temp")

# Scatter plot for 2015 record-breaking temperatures
plt.scatter(df_15_max.index[df_15_max["Data_Value"] > df_05_14_max["Data_Value"]],
            df_15_max["Data_Value"][df_15_max["Data_Value"] > df_05_14_max["Data_Value"]],
            color="darkred", label="2015 Record Highs")
plt.scatter(df_15_min.index[df_15_min["Data_Value"] < df_05_14_min["Data_Value"]],
            df_15_min["Data_Value"][df_15_min["Data_Value"] < df_05_14_min["Data_Value"]],
            color="dodgerblue", label="2015 Record Lows")

# Fill area between max and min temperatures
plt.fill_between(range(365), df_05_14_min["Data_Value"], df_05_14_max["Data_Value"], color="lightblue", alpha=0.3)

# Add labels, legend, and month ticks
plt.legend()
plt.xticks([0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334], month_abbr[1:])
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Records (2005-2014) and 2015 Record Breakers")
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()