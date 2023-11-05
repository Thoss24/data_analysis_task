import pandas as pd
import csv
import math
import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

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

#good < 50
#satisfactory > 50 < 100
#moderate > 100 < 150
#poor > 150 < 300
#very poor > 400 < 500
#severe > 500

#print(df)

for x in df.index:
    # set mean of AQI if value is missing
    if math.isnan(float(df.loc[x, "AQI"])):
        df.loc[x, "AQI"] = df.loc[x, ["PM2.5","PM10","NO","NO2","NOx","NH3","CO","SO2","O3","Benzene","Toluene","Xylene"]].mean()
#     # set AQI_
#     if df.loc[x, "AQI"] > 500:
#         df.loc[x, "AQI_Bucket"] = "Severe"
#     if df.loc[x, "AQI"] > 400 and df.loc[x, "AQI"] < 500:
#         df.loc[x, "AQI_Bucket"] = "Very Poor"
#     if df.loc[x, "AQI"] > 150 and df.loc[x, "AQI"] < 300:
#         df.loc[x, "AQI_Bucket"] = "Poor"
#     if df.loc[x, "AQI"] > 100 and df.loc[x, "AQI"] < 150:
#         df.loc[x, "AQI_Bucket"] = "Moderate"
#     if df.loc[x, "AQI"] > 50 and df.loc[x, "AQI"] < 100:
#         df.loc[x, "AQI_Bucket"] = "Satisfactory"
#     if df.loc[x, "AQI"] < 50:
#         df.loc[x, "AQI_Bucket"] = "Good"

cols = ["PM2.5","PM10","NO","NO2","NOx","NH3","CO","SO2","O3","Benzene","Toluene","Xylene", 'AQI']

df[cols] = df[cols].applymap(np.int64)

df.to_csv("no_aqi_bucket.csv", index=False)

newDf = df.drop(['AQI_Bucket', 'Date', 'City'],  axis="columns")

newDf.to_csv("removed_date_city_aqibucket.csv", index=False)

# #df['AQI_Bucket'] = df['AQI_Bucket'].astype(int)

# print(df)

# grouped = df.groupby('City')

# city_average = grouped.mean()

# city_average.to_csv("clean.csv")

# #city_average[cols] = city_average[cols].applymap(np.int64)


# # for index, row in df.iterrows():
# #     print(row['AQI'], row['AQI_Bucket'])

# df.drop(['City', 'Date'], axis=1, inplace=True)

# array = df.values
# x = array[:,0:13]
# x = x.astype('int')
# y = array[:,13]
# #y = y.astype('int')

# # #print(city_average)

# #chi squared = cell (O-E) squared / E
# # sum of all cells of O-E squared / E

# test = SelectKBest(score_func=chi2, k=4)
# fit = test.fit(x, y)

# np.set_printoptions(precision=3)
# print(fit.scores_)

# features = fit.transform(x)
# print(features)