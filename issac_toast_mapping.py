from bs4 import BeautifulSoup
import urllib.request
from dotenv import load_dotenv # .env파일에서 키와 value를 읽어 환경 변수에 추가 
import os # 환경변수는 os 모듈의 environ 속성을 통해 접근 가능
import json
import folium


def make_store_list(): 
    url = "http://www.isaacs.co.kr/bbs/board.php?bo_table=branches&page="
    page_num = 1        # 추출할 페이지 수
    store_list = []     # 매장 위치 정보를 저장할 리스트 



    for page in range(page_num):
        page_idx = page + 1 # page는 1부터 시작
        sourcecode = urllib.request.urlopen(url + str(page_idx)).read() 
        # urlopen은 url을 받아서 html을 return함. 
        soup = BeautifulSoup(sourcecode, 'html.parser')
    
        for i in soup.find_all('td', 'td_subject'): # td, td_subject: 주소를 감싸는 태그와 클래스. find_all 에 두 개 이상의 parameter가 있는 경우 AND처리  
            temp_text = i.get_text() # get_text: 감싸고 있는 태그를 제외한 컨텐츠만 반환함
            store_list.append(temp_text)


    return store_list


def search_map(search_text): # text 주소를 받아서 위경도 값을 포함한 str(json) 파일을 반환: 이후 반환한 객체를 json화 해야 함. 
    
    encodedText = urllib.parse.quote(str(search_text))  # string과 같은 타입의 매개변수를 url로서 유효한 문자로 인코딩해줌 


    url = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query="+ encodedText # 네이버 오픈API 활용 

    load_dotenv() # 환경 변수에 접근 가능하게 해주는 함수. CLIENT ID와 같은 정보를 환경변수로서 관리함으로써  코드를 공개했을 때 이를 은닉할 수 있다.  
    client_id = os.environ.get("CLIENT_ID")
    client_key = os.environ.get("CLIENT_KEY")

    requested = urllib.request.Request(url)
    requested.add_header('X-NCP-APIGW-API-KEY-ID', client_id)
    requested.add_header('X-NCP-APIGW-API-KEY', client_key)

    response = urllib.request.urlopen(requested)
    response_code = response.getcode() # 응답 코드를 반환. 200이면 잘 연결된 것. 

    if(response_code == 200):
        response_body = response.read()
        return response_body.decode('utf-8')
    else:
        print("Error code: ", response_code)



def make_location(store_list): # 위도 경도를 추출해서 x, y리스트에 각각 반환
    x = []
    y = []

    for store_addr in store_list:
        map_data = search_map(store_addr)
        map_data_json = json.loads(map_data) # json 형식으로 변환 
    
        try:
            geocoded_data = map_data_json['addresses'][0]  # 위경도 값을 포함하고 있는 인덱스 
            x.append(float(geocoded_data['x']))
            y.append(float(geocoded_data['y']))

        except IndexError:
            pass

    return x, y 



def make_marker(map_osm, x, y):
    location_num = len(x)
    for i in range(location_num):
        folium.Marker([y[i], x[i]]).add_to(map_osm) # 지도에 해당 위경도에 마카를 추가함. 



if __name__ == "__main__":
    
    store_list = make_store_list() # 이삭 토스트 홈페이지에서 매장 정보를 크롤링 한 뒤 

    x_list, y_list = make_location(store_list) # 네이버 오픈 api Geocoding을 활용하여 위경도 값을 뽑아온다. 

    map_osm = folium.Map(location = [37.5, 127.0]) # 서울을 중심으로 지도를 열어서

    make_marker(map_osm, x_list, y_list) # 지도에 이삭토스트 매장 위치에 마카를 찍는다. 

    map_osm.save('issac_store.html') # 결과를 html 파일에 save! 