from utilities.configurations import *
def bookAPIPayload(isbn):
    body ={

        "name":"Learn Appium Automation with Java",
        "isbn":isbn,
        "aisle":"227",
        "author":"John foe"
    }
    return body


def getPayloadFromDB(query):
    # tableData = getQuery(query)
    addBook = {}
    tableData = getQueryFetchAll(query)
    for data in tableData:
        if data[0] == 'Selenium':
            addBook = {
                "name": data[0],
                "isbn": data[1],
                "aisle": data[2],
                "author": data[3]
             }
            break
    return addBook