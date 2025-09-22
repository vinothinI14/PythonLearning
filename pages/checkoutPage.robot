*** Settings ***
Documentation    Checkout page functionality
Library    SeleniumLibrary
Resource    ../pages/generic.robot

*** Variables ***
${countryName}=    India

*** Keywords ***
Complete product checkout
    Click Element    xpath://button[@class='btn btn-success']
    Input Text    id:country    ${countryName}
    Wait Until Element Is Visible    xpath://a[text()='${countryName}']    10
    Click Element    xpath://a[text()='${countryName}']
    Sleep    5
    Click Element   //label[@for='checkbox2']
    Click Element    xpath://input[@value='Purchase']

Validate product has been successfully ordered
    Page Should Contain    Success!


    
    
