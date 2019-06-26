import json
import requests
#!/usr/bin/env python

# Make a get request with the parameters. 08-11-96-54-F3-E4
response = requests.get("https://api.macaddress.io/v1?apiKey=at_gVL2VUlnXzRjD9mkj70Avd6bqgdkm&output=json&search=44:38:39:ff:ef:57")

# Print the content of the response (the data the server returned)
print(response.content)
python_dict_string=json.loads(response)

r = json.dumps(str(response.content.splitlines()))
print(r)
file = open("testfile.txt","w")
json_string = json.dumps(response.content)
python_dict_string=json.loads(json_string)
print (python_dict_string['response'])
file.write(r)
file.close()
