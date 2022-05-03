# "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={c2a9974f036e293277cb27f2a256a035}"

import requests
import json
import os 
from dotenv import load_dotenv


load_dotenv()

weather_api_key = os.environ.get('WEATHER_API_KEY')
city = "California"
lang = "kr"
unit = "metric"

api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&lang={lang}&units={unit}"

result = requests.get(api) # api 서버에 request 요청을 보냄. 날씨 결과를 html파일로 받음 

print(result.text)

data = json.loads(result.text) # 날씨 데이터를 json화 

print(data["name"], "의 날씨입니다.")
print(data["weather"][0]["main"])
print("현재 온도는 ", data["main"]["temp"], "입니다.")
print("최고 기온:", data["main"]["temp_max"] )
print("습도: ", data["main"]["humidity"] )
print("기압", data["main"]["pressure"] )
print("풍속: " , data["wind"]["speed"]) 