from dotenv import load_dotenv
import os 
import json
import requests

load_dotenv()

rest_api_key = os.getenv('REST_API_KEY')

with open("kakao_token.json", "r") as json_file:
    tokens = json.load(json_file) # 토큰을 같이 보낼 거임. 토큰 = 자유이용권  

url = "https://kapi.kakao.com/v2/api/talk/memo/default/send" # 요청을 보낼 url 

headers={
    "Authorization": "Bearer " + tokens["access_token"] # 메시지와 함께 보낼 access_token
}

data = {
    "template_object": json.dumps({
        "object_type": "text", # 객체의 타입은 text 
        "text":"hello world!",
        "link":{
            "web_url": "https://sogang.ac.kr"
        }  
    })
}

response = requests.post(url, headers=headers, data=data)

print(response.status_code)


