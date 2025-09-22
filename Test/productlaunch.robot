*** Settings ***
Documentation    vel vilakku promotion
Library    SeleniumLibrary

*** Test Cases ***
Promote vel vilakku product
    Open magic url and click link
    
*** Variables ***
@{urls}    https://www.amazon.co.in/s?url=search-alias%3Daps&field-keywords=Arumugam+vel+vilakku&field-brand=VelMuru&field-asin=B0FNX6B72K    https://www.amazon.co.in/s?url=search-alias%3Daps&field-keywords=Arumuga+vilakku+with+vel&field-brand=VelMuru&field-asin=B0FNX6B72K    https://www.amazon.co.in/s?url=search-alias%3Daps&field-keywords=vel+vilakku&field-brand=VelMuru&field-asin=B0FNX6B72K    https://www.amazon.co.in/s?url=search-alias%3Daps&field-keywords=Sashti+pooja+vilakku&field-brand=VelMuru&field-asin=B0FNX6B72K    https://www.amazon.co.in/s/ref=nb_sb__noss_2?url=search-allias%3Daps&field-keywords=Saravanabava+vilakku&field-brand=VelMuru&field-asin=B0FNX6B72K    https://www.amazon.co.in/s/ref=nb_sb__noss_2?url=search-allias%3Daps&field-keywords=Panjakavya+vilakku&field-brand=VelMuru&field-asin=B0FNX6B72K    https://www.amazon.co.in/s/ref=nb_sb__noss_2?url=search-allias%3Daps&field-keywords=Brass+diya+for+pooja&field-brand=VelMuru&field-asin=B0FNX6B72K
*** Keywords ***
Open magic url and click link
    Create WebDriver    Chrome
    FOR    ${url}    IN    @{urls}
        Go To    ${url}
        Maximize Browser Window
        Sleep    5
    END
#    Click Element    xpath://a[contains(@href,'https://www.amazon.co.in')]

