# Testing Documentation

## Table of Contents

* [Testing](#testing)
* [Validation](#validation)
* [Return to README](/README.md)

# Testing

## Manual Testing

As a means of testing functionality manual testing was carried out on the web application.

### Testing Usability

Using the method of acceptance testing by using multiple users to test different portions of the website.

| Testing | Actions | Expected results | Completed | Comments |
|---|---|---|---|---|
|Home Page|---|---|---|---|
|---| Load page | The page should load without errors |y|---|
|---|Icons visible|Clearly indicate icons|y|---|
|---|FeedBack provided| loads |y|---|
|---|Images fade and repeat with no flicker| Images are repeating correctly |y|---|
|Google Sign Up|---|---|---|---|
|---| Load page | The page should load without errors |y|Fixed|
|---|Click on sign up button|Redirected to sign in|y|---|
|---|Verification notice |Email delivered|y|---|
|---|Buttons|Clicking produces result|y|---|
|---|FeedBack provided| loads |y|---|
|FaceBook|---|---|---|---|
|---| Load page | Currently Broken |n| I had all four login options but I reset the database|
|---|Click on sign up button| Currently Broken|n|---|
|---|Verification notice | Currently Broken|n|---|
|---|Buttons| Currently Broken|n|---|
|---|FeedBack provided| Currently Broken |n|---|
|Instagram|---|---|---|---|
|---| Load page | Currently Broken |n| I had all four login options but I reset the database|
|---|Click on sign up button| Currently Broken|n|---|
|---|Verification notice | Currently Broken|n|---|
|---|Buttons| Currently Broken|n|---|
|---|FeedBack provided| Currently Broken |n|---|
|Twitter|---|---|---|---|
|---| Load page | Currently Broken |n| I had all four login options but I reset the database|
|---|Click on sign up button| Currently Broken|n|---|
|---|Verification notice | Currently Broken|n|---|
|---|Buttons| Currently Broken|n|---|
|---|FeedBack provided| Currently Broken |n|---|
|Sign Up|---|---|---|---|
|---|Click on sign up button|Redirected to sign up|y|---|
|---|Entering Details|Inputs fields should work |y|---|
|---|Verification notice |Email delivered|y|---|
|---|Buttons|Clicking produces result|y|---|
|---|FeedBack provided| loads |y|---|
|Sign In|---|---|---|---|
|---|Click on sign up button|Redirected to sign in|y|---|
|---|Entering Details|Inputs fields should work |y|---|
|---|Forgotten Password |Verification Code delivered|y|---|
|---|Buttons, Links|Clicking produces action|y|---|
|---|FeedBack provided| loads |y|---|
|Nav|---|---|---|---|
|---|Dropdown|Dropdown menu slides menu down and up |y|---|
|---|Buttons, Links|Clicking produces action|y|---|
|---|Icons visible|Clearly indicate icons|y|---|
|---|---|---|---|---|
|Mobile Nav Bottom |---|---|---|---|
|---|Search|Should pop up and down when clicked |y|---|
|---|Buttons, Links|Clicking produces action|y|---|
|---|Icons visible|Clearly indicate icons|y|---|
|---|---|---|---|---|
|Menu|---|---|---|---|
|---|Entering Details|Inputs fields should work |y|---|
|---|Buttons, Links|Clicking produces action|y|---|
|---|FeedBack provided| loads |y|---|
|Menu Detail|---|---|---|---|
|---|Entering Details|Inputs fields should work |y|---|
|---|Buttons, Links|Clicking produces action|y|---|
|---|FeedBack provided| loads |y|---|
|Checkout|---|---|---|---|
|---|Entering Details|Inputs fields should work |y|---|
|---|Buttons, Links|Clicking produces action|y|---|
|---|FeedBack provided| loads |y|---|
|Checkout Success|---|---|---|---|
|---|Buttons, Links|Clicking produces action|y|---|
|---|FeedBack provided| loads |y|---|
|Order Confirmation|---|---|---|---|
|---|Emails Sent for Confirmation| Clicking produces action |y|---|
|---|FeedBack provided| loads |y|---|
|Profile|---|---|---|---|
|---| Load page | The page should load without errors |y|---|
|---|Entering Details|Inputs fields should work |y|---|
|---|Buttons, Links|Clicking produces action|y|---|
|---|Icons visible|Clearly indicate icons|y|---|
|Messages|---|---|---|---|
|---| Alerts | All open when activated |y|---|
|---|Success|message pops up providing feedback |y|---|
|---|Warning |message pops up providing feedback |y|---|
|---|Info|message pops up providing feedback |y|---|
|---|Error|message pops up providing feedback |y|---|
|Search|---|---|---|---|
|---| Load page | The page should load without errors |y|---|
|---|Entering Details|Inputs fields should work |y|---|
|---|Buttons, Links|Clicking produces action|y|---|
|---|Icons visible|Clearly indicate icons|y|Intuitive|
|Search Mini |---|---|---|---|
|---| Load page | The page should load without errors |y|---|
|---|Entering Details|Inputs fields should work |y|---|
|---|Buttons, Links|Clicking produces action|y|---|
|---|Icons visible|Clearly indicate icons|y| Intuitive |

<br>

# Validation

Django HTML is throughout the website

HTML: validated using WC3 Validator CSS: validated using Jigsaw W3 Validator

No errors validating html or css

![Validation](documentation/readme_folder/testing/val-1.png)

![Validation](documentation/readme_folder/testing/val-2.png)

![Validation](documentation/readme_folder/testing/val-3.png)

![Validation](documentation/readme_folder/testing/val-4.png)

![Validation](documentation/readme_folder/testing/val-5.png)

![Validation](documentation/readme_folder/testing/val-6.png)

![Validation](documentation/readme_folder/testing/val-7.png)

![Validation](documentation/readme_folder/testing/val-8.png)

### Python

No errors detected. I have pycodestyle installed in my workspace on VSCode and the only errors I'm recieving are for the settings.py file for line too long.

![Python](documentation/readme_folder/testing/python.png)

[Back to Top](#table-of-contents)