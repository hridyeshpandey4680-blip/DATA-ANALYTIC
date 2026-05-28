#1. Import Libraries & Sample Dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Sample dataset
df = sns.load_dataset("tips") # built-in dataset
print(df.head())


# 2. Histogram (Distribution Plot)
plt.figure(figsize=(6,4))
plt.hist(df['total_bill'], bins=20)
plt.title("Histogram of Total Bill")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")
plt.show()




#3. Bar Chart (Categorical Data)

plt.figure(figsize=(6,4))
sns.countplot(data=df, x="day")
plt.title("Count of Customers per Day")
plt.show()



#4. Box Plot (Outliers and Distribution)

plt.figure(figsize=(6,4))
sns.boxplot(data=df, y="total_bill")
plt.title("Boxplot of Total Bill")
plt.show()



#5. Line Chart (Trend Over Time)
#Example using simulated data:
sales = pd.DataFrame({
 "month": range(1,13),
 "revenue": np.random.randint(1000, 5000, 12)
})
plt.figure(figsize=(7,4))
plt.plot(sales['month'], sales['revenue'], marker='o')
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()



#6. Scatter Plot (Relationship Between Two Variables)
plt.figure(figsize=(6,4))
sns.scatterplot(data=df, x="total_bill", y="tip")
plt.title("Total Bill vs Tip")
plt.show()


#7. Correlation Heatmap
plt.figure(figsize=(6,4))
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()


#8. Missing Value Heatmap
# Bright color (yellow/green): missing values
# Dark color: non-missing values

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Dataset with NO NaN values
data = {
 'Age': [18, 20, 19, 21, 22],
 'Marks': [85, 90, 78, 88, 92],
 'Attendance (%)': [92, 88, 95, 91, 93],
 'Project Score': [80, 85, 82, 88, 90]
}
df_clean = pd.DataFrame(data)
plt.figure(figsize=(6,4))
sns.heatmap(df_clean.isnull(), cbar=False, cmap="viridis")
plt.title("Missing Data Heatmap (No Missing Values)")
plt.show()



import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# Sample dataframe with missing values
data = {
 'Age': [25, 30, np.nan, 35, 40],
 'Salary': [50000, np.nan, 60000, 55000, np.nan],
 'Department': ['HR', 'IT', 'Finance', np.nan, 'IT']
}
df2 = pd.DataFrame(data)
plt.figure(figsize=(6,4))
sns.heatmap(df2.isnull(), cbar=False, cmap="viridis")
plt.title("Missing Data Heatmap (Class Example)")
plt.show()


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# Simple dataset for teaching
data = {
 'Age': [18, 20, 19, np.nan, 22],
 'Marks': [85, np.nan, 78, 90, 88],
 'Attendance (%)': [92, 88, np.nan, 95, 91],
 'Project Score': [np.nan, 80, 85, 88, 90]
}
df = pd.DataFrame(data)
plt.figure(figsize=(6,4))
sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
plt.title("Missing Data Heatmap")
plt.tight_layout()
plt.show()