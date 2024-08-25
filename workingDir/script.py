


def dataProcessor(df1):
    import pandas as pd
    import matplotlib.pyplot as plt
    print("Here is how our original Dataset looks - ")
    print('\n')
    print(df1)

    print('\n\n\n')

    # df1['Total Food Cost'] = df1['Groceries Index'] + df1['Restaurant Price Index']
    df1['Total Food Cost Index'] = df1.apply(lambda x: x['Groceries Index'] + x['Restaurant Price Index'], axis=1)
    # print df

    df1.rename(columns = {"Cost of Living Plus Rent Index" : "Total Living Cost Index"}, inplace = True, errors = 'raise')

    print("Here is how our new Dataset looks - with added coloumn -  'Total Food Cost Index' and modified column 'Total Living Cost Index' looks")

    print('\n')

    print(df1)

    return df1


def createScatterPlot(df1, name):
    import pandas as pd
    import matplotlib.pyplot as plt

    plt.figure(figsize = (10,10))
    plt.scatter(df1['Total Living Cost Index'], df1['Total Food Cost Index'], c ="blue")

    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")


    plt.scatter(df1['Local Purchasing Power Index'], df1['Total Food Cost Index'], c ="red")



    plt.scatter(df1['Local Purchasing Power Index'], df1['Total Living Cost Index'], c ="green")

    txt="This graph describes 3 different values, IN RED - Local Purchasing Power Index (x-axis) vs. Total Food Cost Index (y-axis), IN GREEN - Local Purchasing Power Index (x-axis) vs. Total Living Cost Index (y-axis), and IN BLUE - Total Living Cost Index (x-axis) vs. Total Food Cost Index (y-axis)"
    plt.figtext(0.5, 0.01, txt, wrap=True, horizontalalignment='center', fontsize=12)

    # plt.show()
    
    plt.savefig(name)


def main():
    import pandas as pd
    
    df1 = pd.read_csv("Cost_of_Living_Index_by_Country_2024.csv")

    print('\n\n\n')

    df1 = dataProcessor(df1)

    createScatterPlot(df1, 'Cost_Index_Analysis.png')

if __name__ == "__main__":
    main()


