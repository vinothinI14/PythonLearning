*** Settings ***
Documentation        To Validate unsuccessful login
Library              SeleniumLibrary
Library              DataDriver    file=TestResources/data.csv    encoding=utf_8   dialect=unix
Test Setup           Open browser with url
Library              SeleniumLibrary
Resource             ../pages/generic.robot
Test Template        Validate unsuccessful login

#*** Test Cases ***    UserName    Password
#Invalid username    testuser      learning
#Invalid password    rahulshettyacademy    testuser
#Special character    @t#4       learning
#
*** Test Cases ***
    [Tags]    REGRESSION
Login with user ${UserName} and password ${Password}        xyc     123456

*** Variables ***
${errorMsg}            css:.alert-danger
${errMsgText}          Incorrect username/password.

*** Keywords ***

Validate unsuccessful login
    [Arguments]         ${UserName}    ${Password}
    Fill the login form        ${UserName}    ${Password}
    Wait till element loaded in the page    ${errorMsg}
    Verify error message
    Close Browser Session

Fill the login form
    [Arguments]         ${UserName}    ${Password}
    Input Text          id:username        ${UserName}
    Input Password      password           ${Password}
    Click Button        signInBtn

Wait till element loaded in the page
    [Arguments]    ${errorMsg}
    Wait Until Element Is Visible         ${errorMsg}

Verify error message
    Element Text Should Be                ${errorMsg}  ${errMsgText}

#*** Settings ***
#Documentation   To validate the Login form
#Library     SeleniumLibrary
#Library     DataDriver      file=TestResources/data.csv     encoding=utf_8   dialect=unix
#Test Teardown   Close Browser
#Test Template   Validate UnSuccesful Login
#
#
#*** Variables ***
#${Error_Message_Login}      css:.alert-danger
#
#*** Test Cases ***
#Login with user ${username} and password ${password}        xyc     123456
#
#
#*** Keywords ***
#Validate UnSuccesful Login
#    [Arguments]     ${username}     ${password}
#    open the browser with the Mortgage payment url
#    Fill the login Form    ${username}      ${password}
#    wait until it checks and display error message
#    verify error message is correct
#
#open the browser with the Mortgage payment url
#    Create Webdriver    Chrome
#    Go To   https://rahulshettyacademy.com/loginpagePractise/
#
#Fill the login Form
#    [arguments]     ${username}     ${password}
#    Input Text          id:username     ${username}
#    Input Password      id:password     ${password}
#    Click Button        signInBtn
#
#wait until it checks and display error message
#    Wait Until Element Is Visible       ${Error_Message_Login}
#
#verify error message is correct
#   ${result}=   Get Text    ${Error_Message_Login}
#   Should Be Equal As Strings     ${result}     Incorrect username/password.
#   Element Text Should Be       ${Error_Message_Login}      Incorrect username/password.
















