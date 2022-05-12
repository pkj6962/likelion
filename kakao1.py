from dotenv import load_dotenv
import os 
import requests
import json 

load_dotenv()

rest_api_key = os.getenv('REST_API_KEY')
authorization_code = os.getenv('authorization_code')

url = 'https://kffasdfauth.kakao.com/oauth/token'

redirect_uri = 'http://127.0.0.1'

data = {
    'grant_type': 'authorization_code',
    'client_id': rest_api_key,
    'redirect_uri': redirect_uri,
    'code': authorization_code
}

response = requests.post(url, data=data)

tokens = response.json()

print(tokens)

with open("kakao_token.json", "w") as json_file:
    json.dump(tokens, json_file)
