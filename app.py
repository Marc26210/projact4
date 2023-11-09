import requests  # Import the requests library for making HTTP requests

API_KEY = 'dc879c8e22929aa89e685069a44aa263'  # Your API key from IPStack

def get_ip_info(api_key):
    # Define a function called get_ip_info that takes an API key as an argument

    url = f"http://api.ipstack.com/check?access_key={api_key}"
    # Build the URL for the IPStack API, including the API key

    try:
        response = requests.get(url)  # Send an HTTP GET request to the API
        response.raise_for_status()  # Raise an exception for HTTP errors

        data = response.json()  # Parse the JSON response from the API

        ipv4 = data.get('ip')  # Extract the IPv4 address from the response
        ipv6 = data.get('ipv6')  # Extract the IPv6 address from the response
        location = f"{data.get('city')}, {data.get('region_name')}, {data.get('country_name')}"
        # Build a location string from city, region, and country name
        country_code = data.get('country_code')  # Extract the country code from the response

        print(f"IPv4 Address: {ipv4}")  # Print the IPv4 address
        print(f"IPv6 Address: {ipv6}")  # Print the IPv6 address
        print(f"Location: {location}")  # Print the location
        print(f"Country Code: {country_code}")  # Print the country code

    except requests.exceptions.RequestException as req_err:
        # Handle HTTP-related errors
        print(f"HTTP error occurred: {req_err}")

    except Exception as e:
        # Handle other exceptions (e.g., JSON parsing error)
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # If the script is run as the main program:

    get_ip_info(API_KEY)  # Call the get_ip_info function with the API key