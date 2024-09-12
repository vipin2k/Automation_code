*** Settings ***
Library     RequestsLibrary
Library     Collections


*** Variables ***
${base_url}     https://reqres.in/
${user}     2

*** Test Cases ***
Get_user_info
        Create Session    mysession    ${base_url}
        ${response}     Get Request     mysession   /api/users/${user}
        Log To Console      ${response.status_code}
        Log To Console      ${response.content}
        Log To Console      ${response.headers}

        #validation status_code
        ${status_code} =    Convert To String   ${response.status_code}
        Should Be Equal      ${status_code}      200
        
        #validation response_body
        ${response_body} =     Convert To String  ${response.content}
        Should Contain    ${response_body}    janet.weaver@reqres.in

        #validation response_body
        ${conent_type_value} =    Get From Dictionary    ${response.headers}    Connection
        Should Be Equal    ${conent_type_value}    keep-alive
