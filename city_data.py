import pandas as pd
import math

#good < 50
#satisfactory > 50 < 100
#moderate > 100 < 150
#poor > 150 < 300
#very poor > 400 < 500
#severe > 500

df = pd.read_csv("city_day.csv")

df.drop_duplicates(inplace = True)

first = df["PM2.5"].mean()
df["PM2.5"].fillna(first, inplace = True)

second = df["PM10"].mean()
df["PM10"].fillna(second, inplace = True)

third = df["NO"].mean()
df["NO"].fillna(third, inplace = True)

fourth = df["NO2"].mean()
df["NO2"].fillna(fourth, inplace = True)

fifth = df["NOx"].mean()
df["NOx"].fillna(fifth, inplace = True)

sixth = df["NH3"].mean()
df["NH3"].fillna(sixth, inplace = True)

seventh = df["CO"].mean()
df["CO"].fillna(seventh, inplace = True)

eighth = df["SO2"].mean()
df["SO2"].fillna(eighth, inplace = True)

ninth = df["O3"].mean()
df["O3"].fillna(ninth, inplace = True)

tenth = df["Benzene"].mean()
df["Benzene"].fillna(tenth, inplace = True)

eleventh = df["Toluene"].mean()
df["Toluene"].fillna(eleventh, inplace = True)

twelfth = df["Xylene"].mean()
df["Xylene"].fillna(twelfth, inplace = True)

for x in df.index:
    # set mean of AQI if value is missing
    if math.isnan(float(df.loc[x, "AQI"])):
        df.loc[x, "AQI"] = df.loc[x, ["PM2.5","PM10","NO","NO2","NOx","NH3","CO","SO2","O3","Benzene","Toluene","Xylene"]].mean()

    # set AQI_
    if df.loc[x, "AQI"] > 500:
        df.loc[x, "AQI_Bucket"] = "Severe"
    if df.loc[x, "AQI"] > 400 and df.loc[x, "AQI"] < 500:
        df.loc[x, "AQI_Bucket"] = "Very Poor"
    if df.loc[x, "AQI"] > 150 and df.loc[x, "AQI"] < 300:
        df.loc[x, "AQI_Bucket"] = "Poor"
    if df.loc[x, "AQI"] > 100 and df.loc[x, "AQI"] < 150:
        df.loc[x, "AQI_Bucket"] = "Moderate"
    if df.loc[x, "AQI"] > 50 and df.loc[x, "AQI"] < 100:
        df.loc[x, "AQI_Bucket"] = "Satisfactory"
    else: 
        df.loc[x, "AQI_Bucket"] = "Good"


print(df)

#x = df

#print(df.to_string())