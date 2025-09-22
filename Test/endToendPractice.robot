*** Settings ***
Documentation    Order product from ecommerce website
Library    SeleniumLibrary
Library    Collections
Library    ../customLibrary/shop.py
Resource        ../pages/loginPage.robot
Resource    ../pages/shopPage.robot
Resource    ../pages/checkoutPage.robot
Resource             ../pages/generic.robot
Test Setup           Open browser with url

*** Variables ***

${errMsgText}          Incorrect username/password.
@{expectedBrandList}=    iphone X    Samsung Note 8    Nokia Edge    Blackberry
@{actualBrandList}
@{productList}    Samsung Note 8    Blackberry

*** Test Cases ***    
Verify cards title in the shop page
    [Tags]    REGRESSION
    loginPage.Fill the login form        ${UserName}    ${Password}
    shopPage.Extract brand title form the page
    shopPage.Validate and compare the list
    Add Item And Checkout    ${productList}
    Complete product checkout
    Validate product has been successfully ordered

*** Keywords ***
Verify error message
    Element Text Should Be    ${errorMsg}  ${errMsgText}



