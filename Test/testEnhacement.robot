*** Settings ***
Documentation        To Validate login form
Library              SeleniumLibrary
Resource            ../pages/generic.robot
Test Setup           Open browser with url


*** Test Cases ***
Validate unsuccessful login
    [Tags]    SMOKE
    Fill the login form        ${UserName}    ${Password}
    Wait till element loaded in the page    ${errorMsg}   
    Verify error message
    Close Browser Session

*** Variables ***
${errorMsg}            css:.alert-danger
${errMsgText}          Incorrect username/password.


*** Keywords ***
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