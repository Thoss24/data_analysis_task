import pandas as pd
import math
import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

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
        df.loc[x, "AQI_Bucket"] = 6
    if df.loc[x, "AQI"] > 400 and df.loc[x, "AQI"] < 500:
        df.loc[x, "AQI_Bucket"] = 5
    if df.loc[x, "AQI"] > 150 and df.loc[x, "AQI"] < 300:
        df.loc[x, "AQI_Bucket"] = 4
    if df.loc[x, "AQI"] > 100 and df.loc[x, "AQI"] < 150:
        df.loc[x, "AQI_Bucket"] = 3
    if df.loc[x, "AQI"] > 50 and df.loc[x, "AQI"] < 100:
        df.loc[x, "AQI_Bucket"] = 2
    else: 
        df.loc[x, "AQI_Bucket"] = 1

#df['AQI_Bucket'] = df['AQI_Bucket'].astype(int)

#df.drop('AQI_Bucket', axis=1)


grouped = df.groupby('City')

city_average = grouped.mean()

array = city_average.values
x = array[:,0:13]
x = x.astype('int')
y = array[:,12]
y = y.astype('int')


#print(city_average)

#chi squared = cell (O-E) squared / E
# sum of all cells of O-E squared / E

test = SelectKBest(score_func=chi2, k=4)
fit = test.fit(x, y)

np.set_printoptions(precision=3)
print(fit.scores_)

features = fit.transform(x)
print(features[0:23,:])