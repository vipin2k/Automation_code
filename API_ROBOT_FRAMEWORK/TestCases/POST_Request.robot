*** Settings ***
Library     RequestsLibrary
Library     Collections

*** Variables ***

${URL}=   https://reqres.in


*** Test Cases ***
create_user_info
            Create Session    mysession    ${URL}
            ${body} =   Create Dictionary   name=vipinraj123 job=admin
            ${header} =  Create Dictionary     Connection=keep-alive
            ${response} =  Post Request    mysession    /api/users     data=${body}     headers=${header}
            
            Log To Console    ${response.status_code}
            Log To Console    ${response.content}

            #validation
            ${status_code} =    Convert To String    ${response.status_code}
            Should Be Equal    ${status_code}    201

            ${res_body} =   Convert To String    ${response.content}
            Should Contain    ${res_body}    id
