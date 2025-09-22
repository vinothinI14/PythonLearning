*** Settings ***
Documentation        Learning dropdown and web element click
Library              SeleniumLibrary
Library              Collections
#Test Teardown        Close Browser Session

*** Test Cases ***
    
Verify cards title in the shop page
    [Tags]    SMOKE
    Open browser with url
    Fill the login form with all fields        rahulshettyacademy    learning
    Extract brand title form the page
    Validate and compare the list
    Add the product to the cart     Nokia Edge

*** Variables ***
@{expectedBrandList}=    iphone X    Samsung Note 8    Nokia Edge    Blackberry
@{actualBrandList}
${url}=    https://rahulshettyacademy.com/loginpagePractise/

*** Keywords ***
Open browser with url
    Create Webdriver    Chrome
    Go To               ${url}
    Maximize Browser Window

Fill the login form with all fields
    [Arguments]         ${UserName}    ${Password}
    Input Text          id:username        ${UserName}
    Input Password      password           ${Password}
    Select Radio Button    radio    user
    Sleep    5
    Click Button    xpath://button[@id='okayBtn']
    Wait Until Element Is Visible    xpath://select[@class='form-control']    10s
    Select From List By Value    xpath://select[@class='form-control']    teach
    Click Element    terms
    Click Button        signInBtn
    Sleep               6

Extract brand title form the page
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
        
Add the product to the cart
    [Arguments]    ${brandName}
    Scroll Element Into View     xpath://h4[@class='card-title']
    ${brandTitles}=    Get WebElements    xpath://h4[@class='card-title']
    ${index}=    Set Variable    1
    FOR    ${brand}    IN     @{brandTitles}
        ${text}=    Get Text    ${brand}
        Log To Console    ${text}
        Exit For Loop If    '${text}' == '${brandName}'
        ${index}=    Evaluate  ${index}+1
    END
    Click Button    xpath:(//button[@class='btn btn-info'])[${index}]
    ${checkOut}=    Get Text        xpath://a[@class='nav-link btn btn-primary']
    Log To Console    ${checkOut}

