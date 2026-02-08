## Project Overview
This project automates the signup process of the Authorized Partner portal using Selenium with Python.


## Tools & Technologies Used
  Programming Language: Python
  Automation Tool: Selenium 
  Browser: Google Chrome
  Driver Manager: webdriver-manager
  IDE: VS Code
  OS: Windows


## Project Structure
qa-signup-automation/
├── hello_browser.py
├── signup_automation_script.py
└── README.md


## Automated Test Flow
The automation script performs the following steps:
1. Chrome opened
2. Home page opened
3. Clicked Login
4. Then Clicked Sign Up
5. Opened Register page directly
6. Terms of Services and Privacy Policy accepted
7. Clicked Continue
8. Reached Set up your Account page
9. Account details filled
   - First Name
   - Last Name
   - Email
   - Phone Number
   - Password
   - Confirm Password
10. Reached at Email Verification and Stop at there



## Prerequisites
 Python 3.x installed


## How to Run the Script
1. Open the project folder in VS Code
2. Open terminal
3. Install dependencies:python -m pip install selenium webdriver-manager
4. Run the automation script: python signup_automation_script.py


## Expected Result
  Browser opens automatically
  Signup steps are completed
  Account details are filled automatically
  Script stops at Email Verification page
  Browser closes after a delay in furture stepd

