import pandas as pd
import matplotlib.pyplot as plt


df1 = pd.read_csv("Cost_of_Living_Index_by_Country_2024.csv")

# print(df1)

# df1['Total Food Cost'] = df1['Groceries Index'] + df1['Restaurant Price Index']
df1['Total Food Cost Index'] = df1.apply(lambda x: x['Groceries Index'] + x['Restaurant Price Index'], axis=1)
# print df

df1.rename(columns = {"Cost of Living Plus Rent Index" : "Total Living Cost Index"}, inplace = True, errors = 'raise')
print(df1)

# x =[5, 7, 8, 7, 2, 17, 2, 9,
#     4, 11, 12, 9, 6] 
 
# y =[99, 86, 87, 88, 100, 86, 
#     103, 87, 94, 78, 77, 85, 86]
 
plt.scatter(df1['Total Living Cost Index'], df1['Total Food Cost Index'], c ="blue")

plt.show()