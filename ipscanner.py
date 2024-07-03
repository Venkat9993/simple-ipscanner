#Simple ip scanner using  python  @Venkat9993
import socket
import sys
import requests
import json

# Get the IP address of the host
gethostby = socket.gethostbyname(sys.argv[1])
print("\nThe IP Address of " + sys.argv[1] + " is: " + gethostby + "\n")

# Use the IP address to get location details
req_two = requests.get("https://ipinfo.io/" + gethostby + "/json")
resp_ = json.loads(req_two.text)

print("Location: " + resp_["loc"])
print("Region: " + resp_["region"])
print("City: " + resp_["city"])
print("Country: " + resp_["country"])

