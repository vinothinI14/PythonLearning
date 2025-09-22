*** Settings ***
Documentation    Shop page functionality
Library    SeleniumLibrary
Resource    generic.robot
Library    Collections

*** Variables ***
@{actualBrandList}
@{expectedBrandList}=    iphone X    Samsung Note 8    Nokia Edge    Blackberry

*** Keywords ***
Extract brand title form the page
    Wait Until Element Is Visible    xpath://h4[@class='card-title']
    Scroll Element Into View     xpath://h4[@class='card-title']
    ${brandTitles}=    Get WebElements    xpath://h4[@class='card-title']
    FOR    ${brand}    IN     @{brandTitles}
        ${text}=    Get Text    ${brand}
        Log To Console    ${text}
        Append To List    ${actualBrandList}     ${text}
        Log To Console    ${actualBrandList}
    END

Validate and compare the list
    Lists Should Be Equal    ${expectedBrandList}    ${actualBrandList}