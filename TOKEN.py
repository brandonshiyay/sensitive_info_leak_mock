# Import the requests library for HTTP requests
import requests

# Mock API token for the y4y.mock domain
API_TOKEN = "token_123456789abcdef"

# Endpoint that requires the API token for y4y.mock
data_endpoint = "https://api.y4y.mock/data"

# Function to fetch data from y4y.mock using the API token
def fetch_data(api_token):
    headers = {"Authorization": f"Bearer {api_token}"}
    # Making a GET request to the endpoint with the API token in the header
    response = requests.get(data_endpoint, headers=headers)

    if response.status_code == 200:
        print("Successfully fetched data from y4y.mock.")
        # Process and display the fetched data
        data = response.json()
        print(data)
    else:
        print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")

# Main function to demonstrate the risk of embedding an API token in source code
def main():
    print("Attempting to fetch data from y4y.mock with an embedded API token...")
    fetch_data(API_TOKEN)

if __name__ == "__main__":
    main()
