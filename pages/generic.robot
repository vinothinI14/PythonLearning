*** Settings ***
Documentation    This file contain all the resusable methods which is used in the framework
Library          SeleniumLibrary


*** Variables ***
${UserName}            rahulshettyacademy
${Password}            learning
${url}                 https://rahulshettyacademy.com/loginpagePractise/
${browserName}         Chrome

*** Keywords ***
Open browser with url
    Create Webdriver    ${browserName}
    Go To               ${url}
    Maximize Browser Window

Close Browser Session
    Close Browser