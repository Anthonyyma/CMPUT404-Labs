import requests

#print version of the requets library
print(requests.__version__)

#get the result of the GET request on the Google homepage
res = requests.get("https://raw.githubusercontent.com/Anthonyyma/CMPUT404-Labs/master/lab1.py")

#print out the text of the Google homepage
print(res.text)
