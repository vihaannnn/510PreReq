# 510PreReq
This Repository is for the Pre-Requisite for the AIPI course 510, created by Vihaan Swapneshkumar Nama.
Make sure you are on the 'main' branch of the project. Other branches provided to see commits and history.

```markdown
# Living Cost, Food Cost and Purchasing Power Trend Analysis

## Introduction
This project aims to analyze the Cost of Living Index by Country data and plot some values into a scatter plot to see their correlation.

## About the Dataset
Dataset obtained from - https://www.kaggle.com/datasets/myrios/cost-of-living-index-by-country-by-number-2024
"
Source: www.numbeo.com/cost-of-living/cpi_explained.jsp

Understanding our Cost of Living Indexes
The cost of living indices provided on this website are relative to New York City (NYC), with a baseline index of 100% for NYC.

Here's a breakdown of each index and its meaning:

Cost of Living Index (Excl. Rent): This index indicates the relative prices of consumer goods like groceries, restaurants, transportation, and utilities. It excludes accommodation expenses such as rent or mortgage. For instance, a city with a Cost of Living Index of 120 is estimated to be 20% more expensive than New York City (excluding rent).
Rent Index: This index estimates the prices of renting apartments in a city compared to New York City. If the Rent Index is 80, it suggests that the average rental prices in that city are approximately 20% lower than those in New York City.
Cost of Living Plus Rent Index: This index estimates consumer goods prices, including rent, in comparison to New York City.
Groceries Index: This index provides an estimation of grocery prices in a city relative to New York City. Numbeo uses item weights from the "Markets" section to calculate this index for each city.
Restaurants Index: This index compares the prices of meals and drinks in restaurants and bars to those in NYC.
Local Purchasing Power: This index indicates the relative purchasing power in a given city based on the average net salary. A domestic purchasing power of 40 means that residents with an average salary can afford, on average, 60% less goods and services compared to residents of New York City with an average salary.
For more details on the weights and formulas used, please refer to: www.numbeo.com/common/motivation_and_methodology.jsp


An index of 100 reflects the same living cost as in New York City, United States.
As of 2024 Mid Year data, in NYC,
A family of four estimated monthly costs are $6,074.40 without rent.
A single person's estimated monthly costs are $1,640.90 without rent.
" 
- Directly Quoted from Kaggle Dataset owner - can be found - https://www.kaggle.com/datasets/myrios/cost-of-living-index-by-country-by-number-2024


## Prerequisites
This project requires the use of a Python virtual environment to manage dependencies and ensure consistent behavior across different systems. This guide provides step-by-step instructions for setting up a virtual environment on both Windows and Mac, as well as installing dependencies via a `requirements.txt` file.
- Python 3.x installed on your system.
- Git installed on your machine
- Basic knowledge of command-line operations.

## Cloning the Project
- Open the Command Shell or Terminal on your machine and execute the following command
   ```sh
   git clone https://github.com/vihaannnn/510PreReq.git
   ```


## Setting Up a Virtual Environment

### Windows

1. **Open Command Prompt or PowerShell**:
   - Search for `cmd` or `PowerShell` in the start menu and open it.

2. **Navigate to your project directory**:
   cd (move) into your specific project path (where you have saved it on your computer), example - 
   ```sh
   cd /510PreReq
   ```

3. **Create a virtual environment**:
   ```sh
   python -m venv venv
   ```
   This creates a directory named `venv` that contains the virtual environment.

4. **Activate the virtual environment**:
   ```sh
   .\venv\Scripts\activate
   ```
   After activation, your command prompt will show `(venv)` indicating the virtual environment is active.

### Mac

1. **Open Terminal**:
   - You can find Terminal in your Applications > Utilities folder.

2. **Navigate to your project directory**:
   cd (move) into your specific project path (where you have saved it on your computer), example - 
   ```sh
   cd /510PreReq
   ```

3. **Create a virtual environment**:
   ```sh
   python3 -m venv venv
   ```
   This creates a directory named `venv` that contains the virtual environment.

4. **Activate the virtual environment**:
   ```sh
   source venv/bin/activate
   ```
   After activation, your terminal prompt will show `(venv)` indicating the virtual environment is active.

## Installing Dependencies

1. **Ensure your virtual environment is activated**:
   - Verify that `(venv)` is present in your terminal/command prompt.

2. **Install the dependencies from `requirements.txt`**:
   ```sh
   pip install -r requirements.txt
   ```
   This command installs all the packages listed in the `requirements.txt` file into your virtual environment.

## Deactivating the Virtual Environment

- Once you're done working, you can deactivate the virtual environment by running:
  ```sh
  deactivate
  ```
  After deactivation, the `(venv)` prefix will disappear from your terminal/command prompt.

## To run the project
Go into the workingDir directory and run the script.py file.
The code to do so is - 
```sh
  cd 510PreReq/workingDir
  python script.py
  ```

## To run the test cases of the project
Go into the main directory and run the testing commands.
4 test cases should execute and pass.
If the tests all show up as green -> all tests are running fine
```sh
  cd 510PreReq
  pytest -v
  ```


## Credits
Part of this README.md file was generated using the Artificial Intelligence agent - ChatGPT
Dataset obtained from - https://www.kaggle.com/datasets/myrios/cost-of-living-index-by-country-by-number-2024
Alternate Dataset Source - www.numbeo.com/cost-of-living/cpi_explained.jsp
For more information on the formulas used for the dataset, please refer to: www.numbeo.com/common/motivation_and_methodology.jsp
Data scraped from Numbeo: www.numbeo.com/cost-of-living/rankings_by_country.jsp
All credits to Numbeo: www.numbeo.com/cost-of-living/
```