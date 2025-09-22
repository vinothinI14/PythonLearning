*** Settings ***
Documentation        To Validate login form
Library              SeleniumLibrary

*** Test Cases ***
Validate unsuccessful login
    Open browser with url
    Fill the login form
    Wait till error message displayed
    Verify error message

*** Keywords ***
Open browser with url
    Create Webdriver    Chrome
    Go To               https://rahulshettyacademy.com/loginpagePractise/
 
Fill the login form
    Input Text          id:username        RahulshettyAcademy
    Input Password      password           Testpassword
    Click Button        signInBtn

Wait till error message displayed
    Wait Until Element Is Visible        css:.alert-danger

Verify error message
    ${errMsg}    Get Text             css:.alert-danger
    Should Be Equal As Strings        ${errMsg}    Incorrect username/password.