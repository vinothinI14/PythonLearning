*** Settings ***
Documentation    Learn window handles
Library          SeleniumLibrary
Library    String
Library    Collections
Resource            ../pages/generic.robot
Test Setup           Open browser with url

*** Test Cases ***
Validate the child window functionality
    Select the link of child window
    Verify the user switched to child window
    Grab email from the child window
#    Enter the email in the parent window

*** Variables ***
*** Keywords ***
Select the link of child window
    Click Element    css:.blinkingText
    sleep    6

Verify the user switched to child window
    Switch Window    NEW
    Title Should Be    RS Academy
    
Grab email from the child window
    ${para}=    Get Text    xpath://p[@class='im-para red']
    @{words}=    Split String    ${para}    at
    ${textfromlist}    Get From List    ${words}    1
    ${word2}=    Split String    ${textfromlist}
    ${email}=    Get From List    ${word2}    0 
    Set Global Variable    ${email}
    Log    ${email}

