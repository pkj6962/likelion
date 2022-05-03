
# smtp: simple mail transfer protocol 

import smtplib # smtp protocol과 관련된 라이브러리 
from email.message import EmailMessage
import imghdr # 이미지 확장자를 판단해주는 모듈
import re # 정규표현식 모듈 
import os
from dotenv import load_dotenv 


# 1. smtp 서버에 연결
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465  # 포트는 문과 같은 것. 같은 주소에 여러 개의 문이 있을 수 있음

def sendEmail(addr, message):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"

    if bool(re.match(reg, addr)): 
        smtp.send_message(message) 
        print("Successfully sended")   
    # 3. 메일을 보낸다. --> send_message(메일의 내용)
    else:
        pass


"""
이메일 유효성 검사: 정규표현식


^:시작, $:끝 
[문자]{해당문자 등장 횟수}


 [a-zA-Z0-9.+_-] : 소문자 대문자 숫자 기호(4개) ex) codelion.Example  counter-ex (계정이름)

 + : 앞에 나온 조건이 최소 한개 이상 존재한다(+가 없다면 문자 하나만 와야 조건에 부합)
 
 @: @가 붙는다

 [a-zA-z0-9]+ : 대문자소문자숫자 중 하나가 1회 이상 반복된다.  (naver 등)

 \.   : escape 문자로써 실제 .(dot) 이 옴을 표현

 [a-zA-z]{2,3}: 최소2회, 최대3회 반복된다. (com, net 등)

 ^ $

"""


if __name__ == '__main__':

    smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) #SSL: security socket layer. 그냥 SMTP 메소드를 쓰면 connection unexpectedly closed 에러가 발생한다. 추가적인 암호화 처리가 포함된 메소드다.  


    load_dotenv()
    ID = os.environ.get("MAIL_ID")
    PW = os.environ.get("MAIL_PW")
    smtp.login(ID, PW) #login(아이디, PW) --> 로그인시켜줌. 


    message = EmailMessage() # 메세지를 담는 통을 만든 것

    #   2. 이메일에 내용을 담는다. 제목과 발신자, 수신자도 담아야 한다. 
    content = "이 텍스트도 전송이 될까요 "



    # close 없이 안전하게 파일을 열고 닫을 수 있는 모듈 
    with open("karina.jpg", "rb") as image: # 이미지 읽기: rb -  read(Write) binary
        image_file = image.read()
    image_type = imghdr.what("karina", image_file) #imghder.what (파일이름, 파일) -> 이미지의 확장자를 추출해주는 모듈 

    message.set_content(content) # 본문(text)을 담음
    message.add_attachment(image_file, maintype="image",subtype=image_type) # text 이외의 파일을 담음. 이미지를 넣고 싶을 때는 mixed_type의 형식으로 보냄. 
    
    # Header(subject, from, to) 에 모두 담는다. --> 제이슨 형식으로 저장되는 듯. 
    message["Subject"] = "[긴급]: 대면수업 전환의 건"
    message["From"] = "pkj6962@gmail.com"
    message["To"] = "pjh6962@naver.com"

    sendEmail("pjh6962@naver.com", message)

    #로그아웃
    smtp.quit()


