import requests
response = requests.get('https://api.github.com')
print(response.status_code, end='\n')  # Check the status code of the response
print(response.json(), end='\n')        # Print the JSON response content