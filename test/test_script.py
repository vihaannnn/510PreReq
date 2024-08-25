from workingDir.script import dataProcessor, createScatterPlot
import pandas as pd
import pytest


@pytest.fixture
def createDf():
    """
    Function which is a python fixture to create mock-data that is required for testing purposes.
    This fixture is injected into all other test methods as a pre-requisite set of instructions before running other test cases.
    """
    mockData = {
        "Rank" : [1],
        "Country" : ["Switzerland"],
        "Cost of living Index" :[101.1],
        "Rent Index" : [46.5],
        "Cost of Living Plus Rent Index" : [74.9],
        "Groceries Index" : [109.1],
        "Restaurant Price Index" : [97.0],
        "Local Purchasing Power Index" : [158.7]
    }

    df = pd.DataFrame(mockData)

    return df

def test_dataProcessor_TLCIndex(createDf):
    """
    Test to determine if the 'Cost of Living Plus Rent Index' column in the original dataset was correctly renamed.
    """
    processedDf = dataProcessor(createDf,'test/Test_Processed_Cost_of_Living_Index_by_Country_2024.csv')

    assert 'Total Living Cost Index' in processedDf.columns, "Column not present"

def test_dataProcessor_TFCIndex(createDf):
    """
    Test to determine if the 'Total Food Cost Index' column in the dataset was correctly created.
    """
    processedDf = dataProcessor(createDf,'test/Test_Processed_Cost_of_Living_Index_by_Country_2024.csv')
    assert 'Total Food Cost Index' in processedDf.columns, "Column not present"

def test_processedDataset_save_check(createDf):
    """
    Test to determine if the processed csv was correctly created and saved accordingly.
    """
    import os
    processedDf = dataProcessor(createDf,'test/Test_Processed_Cost_of_Living_Index_by_Country_2024.csv')
    assert os.path.exists('test/Test_Processed_Cost_of_Living_Index_by_Country_2024.csv'), "Matplotlib File Failed to generate"

def test_createScatterPlot(createDf):
    """
    Test to determine if the graph was correctly created and saved accordingly.
    """
    import os
    processedDf = dataProcessor(createDf,'test/Test_Processed_Cost_of_Living_Index_by_Country_2024.csv')
    createScatterPlot(processedDf,'test/Test_Cost_Index_Analysis.png')
    assert os.path.exists('test/Test_Cost_Index_Analysis.png'), "Matplotlib File Failed to generate"