# Import the requests library for making HTTP requests
import requests

# Mock credentials for the y4y.mock domain
USERNAME = "user_demo"
PASSWORD = "pass_demo123"

# Endpoint for authentication at y4y.mock
auth_url = "https://auth.y4y.mock/login"

# Function to authenticate with y4y.mock using username and password
def authenticate(username, password):
    payload = {
        "username": username,
        "password": password
    }
    response = requests.post(auth_url, data=payload)
    
    if response.status_code == 200:
        print("Authentication successful.")
        access_token = response.json().get('access_token')
        print(f"Access Token: {access_token}")
    else:
        print(f"Failed to authenticate. HTTP Status Code: {response.status_code}")

# Main function to demonstrate the risk of including credentials in source code
def main():
    print("Attempting to authenticate to y4y.mock with username and password...")
    authenticate(USERNAME, PASSWORD)

if __name__ == "__main__":
    main()
