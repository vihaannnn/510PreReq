from workingDir.script import dataProcessor, createScatterPlot
import pandas as pd
import pytest

@pytest.fixture
def createDf():
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
    processedDf = dataProcessor(createDf)

    assert 'Total Living Cost Index' in processedDf.columns, "Column not present"

def test_dataProcessor_TFCIndex(createDf):
    processedDf = dataProcessor(createDf)
    assert 'Total Food Cost Index' in processedDf.columns, "Column not present"

def test_createScatterPlot(createDf):
    import os
    processedDf = dataProcessor(createDf)
    createScatterPlot(processedDf,'test/Test_Cost_Index_Analysis.png')
    assert os.path.exists('test/Test_Cost_Index_Analysis.png'), "Matplotlib File Failed to generate"