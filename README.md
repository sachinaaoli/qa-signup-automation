# QA Signup Automation – Vrit Technologies

## Project Overview
This project automates the **signup process** of the Authorized Partner portal using **Selenium with Python**.

The automation covers the complete signup flow **up to the email verification (OTP) step**.

---

## Tools & Technologies Used
- Programming Language: Python
- Automation Tool: Selenium WebDriver
- Browser: Google Chrome
- Driver Manager: webdriver-manager
- IDE: VS Code
- OS: Windows

---

## Project Structure
qa-signup-automation/
├── hello_browser.py
├── signup_automation_script.py
└── README.md

---

## Automated Test Flow
The automation script performs the following steps:

1. Launches Chrome browser
2. Opens Authorized Partner website
3. Clicks **Get Started**
4. Navigates to Register page
5. Accepts Terms & Conditions
6. Clicks Continue
7. Fills account details:
   - First Name
   - Last Name
   - Email
   - Phone Number
   - Password
   - Confirm Password
8. Clicks **Next**
9. Stops at **Email Verification (OTP) page**

---

## OTP Verification Note
Email verification (OTP) is **not automated** because:
- OTP is sent to a real email inbox
- Backend/email access is required
- This is outside the scope of UI automation

This behavior is **intentional and expected** for QA automation tasks.

---

## Prerequisites
- Python 3.x installed
- Google Chrome browser installed

---

## How to Run the Script

1. Open the project folder in VS Code
2. Open terminal
3. Install dependencies:python -m pip install selenium webdriver-manager
4. Run the automation script:python signup_automation_script.py

---

## Expected Result
- Browser opens automatically
- Signup steps are completed
- Account details are filled automatically
- Script stops at Email Verification page
- Browser closes after a delay

---

## Author
QA Intern Candidate  
(Task Submission for Vrit Technologies)
