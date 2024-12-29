import requests
from config import api_key

# The spreadsheet ID and range
spreadsheet_id = "1dgnH_IIQG_qG50bNb7XZ0_2Fzsl5aO8QdZEF7NxkRuY"
sheet_range = "menuLuna!A1:D42"

# Construct the URL
url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{sheet_range}?key={api_key}"

# Send GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Parse the JSON response
    # print("Sheet Data:")
    # for row in data.get("values", []):
    #     print(row)  # Print each row in the sheet
    source = data.get("values", [])
else:
    print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")
    print(response.text)  # Print error message if any

source.append([])
menu = []
a = []
for i in range(len(source)):
    if not source[i]:
        menu.append(a)
        a = []
    else:
        for t in source[i]:   
            a.append(t)