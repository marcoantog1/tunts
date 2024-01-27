# Readme

## Overview

The **Student Evaluation System** is a Python script designed to evaluate students based on attendance and grades using the Google Sheets API. The script reads data from a specified Google Sheet, performs calculations, and updates the sheet with the evaluation results.

## Prerequisites

Before running the project, ensure you have the following:

- **Python:** Install Python on your machine.
- **Required Packages:** You can install them using the following command:

  ```bash
  pip install gspread oauth2client
  ```

## Configuration

1. **Obtain Google Sheets API Credentials:**
- Go to the Google Cloud Console.
- Create a new project or select an existing one.
- Enable the Google Sheets API for your project.
- Create service account credentials and download the JSON key file.

2. **Save the JSON key file:**
- Save the downloaded JSON key file securely.
- Update the secret_key.json file path in the code with the correct location.

## Running the Project

1. ***Clone the repository:***

  ```bash
  git clone https://github.com/yourusername/your-repo.git
  ```
2. ***Navigate to the project directory:***

  ```bash
  cd your-repo
  ```
3. ***Run the script:***

  ```bash
  python script.py
  ```
This will execute the script and update the specified Google Sheet with the evaluation results.

## Script Explanation
The script iterates through a range of student data in the Google Sheet, calculates the overall grade, and updates the sheet with the evaluation status. The evaluation criteria are as follows:

- If the number of absences is greater than 15, the student is marked as **"Reprovado por Falta"** (Failed due to -absence).
- If the calculated grade is less than 5, the student is marked as **"Reprovado por Nota"** (Failed due to a low grade).
- If the grade is between 5 and 7, the student is marked for an **"Exame Final"** (Final Exam), and the required grade to pass is calculated.
- If the grade is 7 or above, the student is marked as **"Aprovado"** (Approved).
The script prints the evaluation results for each student in the console.

**Note:** Ensure that the specified Google Sheet exists and follows the required format with student information.

Feel free to modify the script or integrate it into your workflow as needed.