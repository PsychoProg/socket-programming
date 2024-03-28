import requests

ip_address = input('enter ip address>')

# url = 'https://rdap.db.ripe.net/ip/5.117.74.229'
# url = "https://api.iplocation.net/?ip={ip_address}"
url = f"https://api.iplocation.net/?ip={ip_address}"
response = requests.get(url)

# Save response data to a JSON file
output_file = 'response.json'
with open(output_file, 'w') as file:
    file.write(response.text)

print(f"Response saved to '{output_file}'.")