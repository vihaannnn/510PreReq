import pandas as pd

df1 = pd.read_csv("Cost_of_Living_Index_by_Country_2024.csv")

# print(df1)

# df1['Total Food Cost'] = df1['Groceries Index'] + df1['Restaurant Price Index']
df1['Total Food Cost Index'] = df1.apply(lambda x: x['Groceries Index'] + x['Restaurant Price Index'], axis=1)
# print df

df1.rename(columns = {"Cost of Living Plus Rent Index" : "Total Living Cost Index"}, inplace = True, errors = 'raise')
print(df1)

