# 510PreReq
This Repository is for the Pre-Requisite for the AIPI course 510, created by Vihaan Nama.

```markdown
# Living Cost, Food Cost and Purchasing Power Trend Analysis

## Introduction
This project requires the use of a Python virtual environment to manage dependencies and ensure consistent behavior across different systems. This guide provides step-by-step instructions for setting up a virtual environment on both Windows and Mac, as well as installing dependencies via a `requirements.txt` file.

## Prerequisites
- Python 3.x installed on your system.
- Basic knowledge of command-line operations.

## Setting Up a Virtual Environment

### Windows

1. **Open Command Prompt or PowerShell**:
   - Search for `cmd` or `PowerShell` in the start menu and open it.

2. **Navigate to your project directory**:
   cd into your specific project path, example - 
   ```sh
   cd path\to\your\project
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
   cd into your specific project path, example - 
   ```sh
   cd /path/to/your/project
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


```

This `README.md` file should help users set up a Python virtual environment on both Windows and Mac, install dependencies, and deactivate the environment when finished.