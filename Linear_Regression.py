import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore", category=UserWarning)


df = pd.read_csv('homeprices.csv')
print(df)


# %matplotlib inline
plt.xlabel('area')
plt.ylabel('price')
plt.scatter(df.area,df.price,color='red',marker='+')
plt.show() 

new_df = df.drop('price',axis='columns')
print(new_df)


price = df.price
print(price)


# Create linear regression object
reg = linear_model.LinearRegression()
reg.fit(new_df,price) #training the model using available dataset.


#(1) Predict price of a home with area = 3300 sqr ft
area = 3300
predicted_price = reg.predict([[area]])
print(predicted_price)


#Y = m * X + b (m is coefficient and b is intercept)
print(reg.coef_)

print(reg.intercept_)

3300*135.78767123 + 180616.43835616432


#(2) Predict price of a home with area = 5000 sqr ft
area = 5000
predicted_price = reg.predict([[area]])
print(predicted_price)