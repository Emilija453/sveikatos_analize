import requests

download_url = "https://dw.euro.who.int/api/v3/export/download/912e2ab65389408ead82ca5be8ed2cac"
save_path = "data_file"  # You can change the filename or path as needed

# Make a GET request to download the file
response = requests.get(download_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Save the content to a file
    with open(save_path, "wb") as file:
        file.write(response.content)
    print("File downloaded successfully.")
else:
    print(f"Failed to download the file. Status code: {response.status_code}")
