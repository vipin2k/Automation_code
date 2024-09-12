*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem  # For reading the file
Library    BuiltIn          # For evaluating the JSON string
Library    String           # For string operations

*** Variables ***
${URL}      https://www.saucedemo.com/v1/index.html
${BROWSER}  Chrome
${JSON_FILE}    D:/API_ROBOT_IN_UI/Configuration/file.json  # Correct path to your JSON file

*** Test Cases ***
Login and Add Items to Cart Using JSON Data
    # Read JSON file content as a string
    ${json_string}=    Get File    ${JSON_FILE}

    # Ensure that the JSON string is correctly formatted
    Log To Console    JSON String: ${json_string}

    # Parse JSON content
     ${json_data}=    Evaluate    import json; json.loads('''${json_string}''')    json

    # Extract data from JSON
    ${name}=    Set Variable    ${json_data['username']}
    ${password}=    Set Variable    ${json_data['password']}

    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Input Text    //*[@type="text"]    ${name}
    Input Text    //*[@type="password"]    ${password}
    Click Element    //*[@type="submit"]
    Sleep    2s

    # Verify successful login by checking the page title
    ${title}=    Get Title
    Log To Console    Title: ${title}

    # Capture item names and prices
    ${bag_name}=    Get Text    (//*[@class="inventory_item_name"])[1]
    Log To Console    Bag: ${bag_name}
    ${bag_price}=    Get Text    (//*[@class="inventory_item_price"])[1]
    Log To Console    Bag Price: ${bag_price}
    Click Element    (//*[@class='btn_primary btn_inventory' and text()='ADD TO CART'])[1]

    ${shirt_name}=    Get Text    (//*[@class="inventory_item_name"])[4]
    Log To Console    Shirt: ${shirt_name}
    ${shirt_price}=    Get Text    (//*[@class="inventory_item_price"])[4]
    Log To Console    Shirt Price: ${shirt_price}
    Click Element    (//*[@class='btn_primary btn_inventory' and text()='ADD TO CART'])[4]

    # Go to the cart
    Click Element    //*[@data-icon="shopping-cart"]
    Sleep    1s

    # Calculate the total
    ${total}=    Evaluate    float(${bag_price.replace('$','')) + float(${shirt_price.replace('$',''))
    Log To Console    Calculated Total: $${total}

    # Proceed to continue shopping
    Click Element    //*[@class="btn_secondary" and text()="Continue Shopping"]
    Sleep    1s

    # Click the drop down
    Click Element   (//*[@class="product_sort_container"]/option["Price (high to low)"])[4]

    # Get the number of items with the specified class name
    ${item_count}=    Get Element Count    //*[@class="inventory_item_name"]
    Log To Console    Total items: ${item_count}

    # Using for loop to get all shirt names
    FOR    ${index}    IN RANGE    1    ${item_count+1}
        ${product_name}=    Get Text    (//*[@class="inventory_item_name"])[${index}]
        Log To Console    Product ${index}: ${product_name}
    END

    # Logout
    Click Element   //*[@class="bm-burger-button"]
    Click Element   (//*[@class="bm-item menu-item"])[3]
