import requests
response = requests.get("https://ipinfo.io")
data = response.json()

print("IP:", data.get("ip"))
print("City:", data.get("city"))
print("Region:", data.get("region"))
print("Country:", data.get("country"))
print("Location (lat,long):", data.get("loc"))

