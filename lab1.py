import requests

#print version of the requets library
print(requests.__version__)

#get the result of the GET request on the Google homepage
res = requests.get("http://www.google.com")

#print out the text of the Google homepage
print(res.text)