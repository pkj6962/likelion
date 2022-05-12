Web Service
==================

# Web Service
* 하이퍼링크로써 그물처럼 정보(데이터)가 얽히고 설킴.

### URL
정보가 어디에 저장되어 있는가에 대한 위치 정보
### HTTP
* 정보를 통신하기 위한 약속
* 프로토콜
* HTTP 요청의 종류
    * GET: "가져다줘"
        * youtube.com을 가져다 줘 (요청)
        * 응답: 웹페이지
    
    * Post: 
        * 이 데이터를 처리해줘

### HTML
* 정보 자원 자체 

### 서버
* url에 요청이 들어오면 대응되는 응답을 해줌 
* html을 보여줌 

* web browser
    * http 통신
    * html코드를 가독성 좋게 보여줌 

### WEb Service
    * 프로그래머 입장:
        * html과 url을 준비해놓고 요청에 대한 응답을 보낼 수 있는 프로그램 


### Web Framework 
* 프레임워크: 웹서비스를 쉽게 만들어주는 기계 
* 복잡한 문제를 해결하는 데 사용되는 기본 구조 
    * 뼈대, 골자

* 대부분의 웹서비스느 비슷한 골자(설계)를 가짐 == 정형화되어 있음 
    * 로그인, 로그아웃
    * 데이터베이스, HTML, 저장, 삭제, 내부동작 등 
    * 정형화된 설계를 구현하기 위해 미리 개발된 기능 단위 


* 라이브러리와는 무엇이 다른가?
    * 프레임워크는 명확한 목적을 달성하기 위해 이미 설계까지 만들어진 구조
    * 라이브러리는 도구의 모음 
        * 리액트: 프론트엔드 '라이브러리'
        * 그때그때 갖다 씀 
    



### MVC, MTV
* M: Model = DB와의 상호작용
* V: View 사용자와 상호작용 
* C: Control =내부 동작의 논리 
* 설계의 원칙:"디자인 패턴"

* 예: 인스타그램
    * Model: 데이터베이스에서 가져옴 / 데이터베이스에 저장 
    * View: instagram.com get 요청
    * Controller: "여기다 저장해야겠다" "이거 보내줘야겠다"


 ###       
