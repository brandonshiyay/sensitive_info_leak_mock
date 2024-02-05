# Import the requests library to make HTTP requests in Python
import requests

# Mock API key for y4y.mock endpoint
API_KEY = "123456789_SECRET_API_KEY"

# The specific endpoint on y4y.mock that requires the API key for access
endpoint_url = "https://api.y4y.mock/sensitive-data"

# Function to retrieve sensitive data from the y4y.mock endpoint
def get_sensitive_data(api_key):
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    response = requests.get(endpoint_url, headers=headers)
    
    if response.status_code == 200:
        print("Successfully retrieved sensitive data:")
        print(response.json())  # Assuming the response is JSON-formatted
    else:
        print(f"Failed to retrieve data. HTTP Status Code: {response.status_code}")

# Main function to demonstrate the improper handling of an API key
def main():
    print("Attempting to retrieve sensitive data from y4y.mock using an API key...")
    get_sensitive_data(API_KEY)

if __name__ == "__main__":
    main()
