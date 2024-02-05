# Import necessary library for HTTP requests
import requests

# Mock credentials for the y4y.mock domain
USERNAME = "example_user"
PWD = "secure_password123"

# Endpoint for a service requiring authentication at y4y.mock
service_url = "https://service.y4y.mock/protected-resource"

# Function to access a protected resource using username and pwd
def access_protected_resource(username, pwd):
    credentials = {
        "username": username,
        "pwd": pwd
    }
    # Attempting to access the protected resource with credentials
    response = requests.post(service_url, data=credentials)
    
    if response.status_code == 200:
        print("Successfully accessed the protected resource.")
        # Process the response data
    else:
        print(f"Access denied. HTTP Status Code: {response.status_code}")

# Main function demonstrating the embedding of credentials in source code
def main():
    print("Attempting to access a protected resource at y4y.mock with embedded credentials...")
    access_protected_resource(USERNAME, PWD)

if __name__ == "__main__":
    main()
