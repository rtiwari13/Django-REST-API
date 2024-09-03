import requests

# endpoint = "https://httpbin.org/#/Status_codes/200"
# endpoint = "http://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

#API
get_response = requests.get(endpoint, params={"abc":"123"}, json={"query":"Django REST"}) #HTTP request
# print(get_response.text)  # print raw text response 
# print(get_response.status_code)
     
print(get_response.json())
