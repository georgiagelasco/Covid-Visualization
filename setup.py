import requests
import csv
import json

# Function to convert CSV to JSON
def csv_to_json(csv_text):
    lines = csv_text.split('\n')
    result = []
    headers = lines[0].split(',')  # First line is the header
    
    # Loop through each row and convert to an object
    for line in lines[1:]:
        row = line.split(',')
        if len(row) == len(headers):
            obj = {headers[i].strip(): row[i].strip() for i in range(len(headers))}
            result.append(obj)
    return result

# Function to download a file
def download_file(url, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"File saved as {file_name}")
    else:
        print(f"Failed to download the file. Status code: {response.status_code}")

# Function to fetch, process and save both CSV and JSON files
def fetch_and_process_csv(file_id):
    download_url = f'https://drive.google.com/uc?id={file_id}&export=download'
    
    # Download CSV file and save as covid.csv
    download_file(download_url, 'covid.csv')

    # Read the CSV content
    with open('covid.csv', 'r') as file:
        csv_text = file.read()

    # Convert CSV to JSON
    json_data = csv_to_json(csv_text)

    # Save JSON file as covid.json
    with open('covid.json', 'w') as json_file:
        json.dump(json_data, json_file, indent=2)
    print("JSON file saved as covid.json")

# Example usage: Convert CSV from Google Drive, download as both covid.csv and covid.json
file_id = '1X4y6dXKLpJdU7D6zlLX4IJP7-QFwgtv8'
fetch_and_process_csv(file_id)
