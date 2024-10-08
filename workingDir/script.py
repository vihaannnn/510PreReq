def dataProcessor(df1, name):
    """
    This function simply processes the data set as per our requirements. We change the name of the 'Cost of Livinv Plus Rent Index' to 'Total Living Cost Index' for improved readability.
    We also add a new column named 'Total Food Cost Index' where we add up the groceries index as well as the restaurant index. We do so usinf a lambda function which we apply tp the dataframe.
    CSV functions used - Renaming a particular column in the dataframe, Applying a lambda funtion to the dataframe, Saving the new dataframe to a new CSV.
    """
    import pandas as pd
    import matplotlib.pyplot as plt
    import os

    if os.path.exists(name):
        os.remove(name)
    print("Here is how our original Dataset looks - ")
    print('\n')
    print(df1)

    print('\n\n\n')

    df1['Total Food Cost Index'] = df1.apply(lambda x: x['Groceries Index'] + x['Restaurant Price Index'], axis=1)

    df1.rename(columns = {"Cost of Living Plus Rent Index" : "Total Living Cost Index"}, inplace = True, errors = 'raise')

    print("Here is how our new Dataset looks - with added coloumn -  'Total Food Cost Index' and modified column 'Total Living Cost Index' looks")

    print('\n')

    print(df1)

    df1.to_csv(name)

    return df1


def createScatterPlot(df1, name):
    """
    In this function we create a scatter plot of various indexes from our CSV, and plot them onto a graph using different colours to indicate the different correlations we are mapping.
    The graph is then saved to the local file system for easier access for the user.
    """
    import pandas as pd
    import matplotlib.pyplot as plt
    import os

    if os.path.exists(name):
        os.remove(name)

    plt.figure(figsize = (10,10))
    plt.scatter(df1['Total Living Cost Index'], df1['Total Food Cost Index'], c ="blue")

    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")


    plt.scatter(df1['Local Purchasing Power Index'], df1['Total Food Cost Index'], c ="red")



    plt.scatter(df1['Local Purchasing Power Index'], df1['Total Living Cost Index'], c ="green")

    txt="This graph describes 3 different values, IN RED - Local Purchasing Power Index (x-axis) vs. Total Food Cost Index (y-axis), IN GREEN - Local Purchasing Power Index (x-axis) vs. Total Living Cost Index (y-axis), and IN BLUE - Total Living Cost Index (x-axis) vs. Total Food Cost Index (y-axis)"
    plt.figtext(0.5, 0.01, txt, wrap=True, horizontalalignment='center', fontsize=12)
    
    plt.savefig(name)


def main():
    """
    Main function of the program.
    Reads the CSV into a pandas dataframe.
    Processes it.
    Creates the scatter plot.
    Prints the Analysis
    CSV functions used - Reading the CSV into a dataframe.
    """
    import pandas as pd
    
    df1 = pd.read_csv("Cost_of_Living_Index_by_Country_2024.csv")

    print('\n\n\n')

    df1 = dataProcessor(df1, 'Processed_Cost_of_Living_Index_by_Country_2024.csv')

    createScatterPlot(df1, 'Cost_Index_Analysis.png')

    print("Please find the graph generated in the 'workingDir' saved as 'Cost_Index_Analysis.png'")

    print('\n\n\n')
    print("GRAPH ANALYSIS")
    print("Upon Analyzing this graph we notice - with even a small change in the food cost index, the living cost increases linearly, but with a higher slope that then other dependencies (seen from the points in blue)")
    print("If we look at the points in red and green, when the Local Purchasing Power Index increases,the Total Living Cost Index increases lesser compared to the Total Food Cost Index.")
    print("We notice that the red and green points are more scattered compared to the blue ones, which indicates that food and living cost indexes are highly correlated compared to the indvidual indexes and the purchasing power index")

if __name__ == "__main__":
    main()


