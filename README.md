# Authorized Partner Signup Automation

## Overview
This script automates the user registration flow for the Authorized Partner portal. It covers the end-to-end process, including:
* User Sign Up & Form Filling
* OTP Verification (handled automatically via Mailinator)
* Agency Details & Experience Entry
* Document Upload

## Prerequisites
Before running the script, please ensure you have the following set up on your machine:
1. Python 3.x installed.
2. Google Chrome installed.

## Environment Setup
* Language: Python 3
* Library: Selenium WebDriver
* Driver Manager: webdriver_manager

## Installation
Open your terminal or command prompt and install the required libraries:

pip install selenium webdriver-manager

## Configuration
Since this script runs locally, you must update the file paths before running it.

1. Open the script in your editor.
2. Scroll down to the document upload section (near the end of the script).
3. Change the paths below to point to valid PDF files on your own computer:

# Update these paths to match your local files
file_inputs[0].send_keys(r"C:\Users\YourName\Documents\test_file_1.pdf")
file_inputs[1].send_keys(r"C:\Users\YourName\Documents\test_file_2.pdf")

## How to Run
Navigate to the folder containing the script and run:

python signup_automation.py

## Test Data Used
The script uses the following hardcoded test data. You can change these inside the script if needed.
* Email Service: Mailinator
* Email Address: testusers1@mailinator.com
* Password: QaTest@1
* Phone: 9855500111

 OTP Handling: The script opens a new tab to check the Mailinator inbox, extracts the 6-digit code, and switches back to the main tab to verify it.
 
 Waits: The script uses WebDriverWait for most elements but includes time.sleep() for dropdowns where animations might cause interaction issues.