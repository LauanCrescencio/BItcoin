import requests
url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=627287230859488184946c65e93865ce')
response = requests.get(url)
print (response.json())
