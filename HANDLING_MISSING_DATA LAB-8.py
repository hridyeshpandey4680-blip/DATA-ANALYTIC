import pandas as pd

df = pd.read_csv("Bengaluru_House_Data.csv")
print(df.head())

print("--- SHAPE OUTPUT ---")
print(df.shape)

print("--- NULL VALUES OUTPUT ---")
print(df.isnull())

print(df.isnull().sum())

print(df.isnull().sum().sum())

#FILLING NULL VALUES
df1=df.fillna(0)
print(df1)

print(df1.isnull().sum().sum())

print(df.isnull().sum().sum())

df2=df.fillna(5)

print(df2)

#FILLING NULL VALUES WITH PREVIOUS VALUE
df3 = df.ffill() #previous row
print(df3)


df4 = df.ffill(axis=1) #previous column
print(df4)

#FILLING NULL VALUES WITH NEXT VALUE
df5=df.bfill() #next row
print(df5)

df6=df.bfill(axis=1) #next column
print(df6)



#filling different values at null
df7=df.fillna({'society':'abcde','balcony':'efghi'})
print(df7)


df8=df.fillna(value=df['balcony'].mean()) #fill null value by mean value of thet column.
#df8=df.fillna(value=df['balcony'].max())
#df8=df.fillna(value=df['balcony'].min())
print(df8)


#DELETING NULL VALUES
df9=df.dropna() #drop all rows with null values
print(df9)


df10=df.dropna(how='all') #drop entire row if all values are null values.
#df10=df.dropna(how='any') #drop entire row if any value is null values. deafault is "any".
print(df10)



#Replacing the null values
import numpy as np
df11=df.replace(to_replace=np.nan, value = 'POOJA')
print(df11)

df12=df.replace(to_replace='2 BHK', value = '2.2 BHK') #can replace any value.
print(df12)



#Interpolate function
df['balcony']=df['balcony'].interpolate(method='linear') #can replace any value.
print(df)


#In case of consecutive null values we need to provide limit i.e. upto
#when we need to interpolate and we need to give direction: forward
#or backword.

df['balcony']=df['balcony'].interpolate(method='linear',limit=1,limit_direction='forward') #can replace any value.
print(df)