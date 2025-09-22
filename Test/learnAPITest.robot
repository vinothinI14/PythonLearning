*** Settings ***
Library    Collections
Library    RequestsLibrary

*** Variables ***
${baseURI}=    https://rahulshettyacademy.com
${bookID}
${bookName}    learnRobotframeworkFromScratch

*** Test Cases ***
Learn dictionary in robotframework
    &{data}=    Create Dictionary    name=vinothini    place=cuddalore    designation=Sr testAnalyst
    log    ${data}
    Log    ${data}[designation]
    ${dicData}=    Get From Dictionary    ${data}    name
    Log    ${dicData}

Add book into a library
    &{add_Book}=    Create Dictionary    name=${bookName}   isbn=terre    aisle=16557    author=vinothiniK
    ${response}=    POST    ${baseURI}/Library/Addbook.php    json=${add_Book}    expected_status=200
    Log    ${response.json()}
    Dictionary Should Contain Key    ${response.json()}    ID
    ${bookID}    Get From Dictionary    ${response.json()}    ID
    Log    ${bookID}
    Set Global Variable    ${bookID}
    Should Be Equal As Strings    successfully added    ${response.json()}[Msg]

Get book details
    ${response}=    GET    ${baseURI}/Library/GetBook.php?    params=ID=${bookID}    expected_status=200
    Log    ${response.json()}
    Should Be Equal As Strings    ${bookName}    ${response.json()}[0][book_name]

Delete added book from library
    &{deleteBook}=    Create Dictionary    ID=${bookID}
    ${response}=    POST    ${baseURI}/Library/DeleteBook.php    json=${deleteBook}    expected_status=200
    Log    ${response.json()}


    

    
    