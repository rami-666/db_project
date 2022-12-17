import pandas as pd
import requests

# Set the URL for the Django backend
django_url = 'http://127.0.0.1:8000/quickstart/'

# Set the username and password for basic authentication
username = 'admin'
password = '12345678'

# Read the Excel file into a Pandas dataframe
excel_file = 'Book1.xlsx'
df = pd.read_excel(excel_file, sheet_name=None)

# Loop through each sheet in the Excel file
for sheet_name, data in df.items():
    # Format the data as a list of dictionaries
    payload = data.to_dict(orient='records')
    print(payload)

    # Send a POST request to the Django backend with basic authentication
    for k in range(0, len(payload)):
        response = requests.post(django_url + sheet_name, data=payload[k], auth=(username, password))


    # Print the response status code
        print(response.status_code)
        if response.status_code == 400:
            print(response.json())