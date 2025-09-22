*** Settings ***
Documentation    Login page functionality
Library    SeleniumLibrary
Resource    generic.robot

*** Variables ***
${errorMsg}            css:.alert-danger

*** Keywords ***
Fill the login form
    [Arguments]         ${UserName}    ${Password}
    Input Text          id:username        ${UserName}
    Input Password      password           ${Password}
    Click Button        signInBtn

Wait till element loaded in the page
    Wait Until Element Is Visible         ${errorMsg}
