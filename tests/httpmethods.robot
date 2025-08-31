*** Settings ***
Library    RequestsLibrary

*** Variables ***
${BASE_URL}    https://jsonplaceholder.typicode.com

*** Test Cases ***
Get Item For API
    Create Session     myapi    ${BASE_URL}
    ${response}       GET On Session    myapi    /todos/1
    ${status_code}      Convert to String   ${response.status_code}
    Should be equal     ${status_code}    200
    ${body}         Convert to String     ${response.content}
    Should contain     ${body}    delectus aut autem
    ${content}      Convert to String     ${response.headers}
    Should contain     ${content}    application/json; charset=utf-8

Create New Todo Item
    Create Session    myapi    ${BASE_URL}
    ${payload}=       Create Dictionary    userId=1    title=Buy milk    completed=False
    ${response}=      POST On Session    myapi    /todos    json=${payload}
    ${status_code}      Convert to String   ${response.status_code}
    Should be equal     ${status_code}    201
    ${body}         Convert to String     ${response.content}
    Should contain     ${body}    Buy milk
    ${content}      Convert to String     ${response.headers}
    Should contain     ${content}    application/json; charset=utf-8