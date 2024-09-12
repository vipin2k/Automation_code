*** Settings ***
Library     JSONLibrary
Library     OperatingSystem
Library     Collections

*** Test Cases ***
testcase:
    ${json_obj}=    Load JSON From File    D:/API_ROBOT_FRAMEWORK/Jsondata/jsondata.json
    Log To Console    ${json_obj}

    ${name_value} =     get value from json     ${json_obj}     $.firstName
    should be equal     ${name_value[0]}    John

    ${phone_num} =     get value from json     ${json_obj}     $.phoneNumbers[0].number
    should be equal     ${phone_num[0]}    0123-4567-8888

    ${address_list}=     Get Value From Json    ${json_obj}    $.address.postalCode
    ${address}=     Get From List    ${address_list}    0
    Log To Console    Postal Code: ${address}
    Should Be Equal    ${address}    630-0192