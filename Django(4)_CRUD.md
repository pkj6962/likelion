Database
=========

- 클래스로 테이블을 정의
  - 각 속성에 필드 타입을 정의해주어야 한다. 
  - 


- migration
  - 데이터베이스에 변경사항을 반영하는 것 
  - ```python manage.py migrate```
    - 초기화
    - 변경사항 반영
  - ``` python manage.py makemigrations ```
    - 변경사항을 담은 ```migration``` 파일을 만듬
    - 이후에 ```migrate``` 명령어를 통해 이를 데이터베이스에 반영

#
프로젝트를 만들고 최초로  ```runserver```를 하면 다음과 같은 경고 메시지를 출력한다. 이는 초기값을 migrate하지 않아서 출력되는 메시지이다. 
```
You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
```


#
#
### 객체 선언
models.py 에 다음과 같이 테이블 클래스를 생성한 뒤 migrate 하면 클래스에 대응되는 테이블이 DB에 생성된다. 

```
class Blog(models.Model): # Model을 상속받음 --> 테이블을만들것이라는 것을 선언
    title = models.CharField(max_length=200)  # 제목.  
    body = models.TextField() # 본문 
    tag = models.CharField(max_length=50)
    date =  models.DateTimeField(auto_now_add=True)  # 작성날짜 # 자동으로 지금 시간을 추가하겠다. 
    


    def __str__(self):
        return self.title # 블로그 

```

> 궁금한 점: 테이블 구조를 바꿀 때는 makemigrations 명령이 선행되어야 했지만, 인자값(eg. auto_now_add = True)를 바꾸는 것은 수정만으로도 변경사항이 적용되었다. 그 이뉴는 무엇인가? 

> 테이블에 속성을 추가할 때는 ```makemigrations```을 해야하지만 속성을 삭제할 때는 이 작업이 필요 없다. (내가 해봄)

#
#
```makemigrations```을 하면 다음과 같이 json형식의 파일이 생성된다. 

```
class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

```
> - Json형태로 저장됨. 
> - ID 속성이  primary key로서 자동으로 만들어짐.
> - admin 사이트에서 우리가 만든 테이블 객체를 확인할 수 있음. 

#

### *객체 변경하기: 새로운 속성을 추가하는 경우 

기존에 있던 테이블(클래스)에 새로운 속성을 추가하고 makemigrations을 하면 다음과 같은 경고?에러? 메시지가 발생한다. 

```
It is impossible to add a non-nullable field 'tag' to blog without specifying a default. This is because the database needs something to populate existing rows.
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit and manually define a default value in models.py.
Select an option: 
```
  기존의 테이블에 새로운 속성을 추가하면 기존의 튜플들은 그 속성값을 부여받지 못했던 상태이다. 따라서 "기존의 튜플에 입력되는 기본값을 입력하라"는 메세지이다. 
(populate: 덧붙이다, one-off: 단한번의)


#
makemigrations을 하면 다음과 같은 메시지가 프롬프트에 출력된다. 내가 어떤 작업을 수행했는지에 대해 꽤나 사용자친화적으로 출력해줌을 확인할 수 있다. 

```
Migrations for 'blogapp':
  blogapp/migrations/0002_blog_tag.py
    - Add field tag to blog

  blogapp/migrations/0003_remove_blog_tag.py
    - Remove field tag from blog

```



#
#
#

## 새 글 입력하기 

### html form 이용하여 새 글 입력하기  

- ```'새 글 생성'``` a 태그를 타면 ```new.html```로 넘어가서, 
```input``` 태그나 ```textarea``` 태그에 정의된 폼에 제목과 본문을 작성할 수 있다. 

```html
<form action="{% url 'create' %}" method="POST">
    {% csrf_token %}  <!-- 보안문제 해결 기능 토큰-->
    <div>
        <label for="title">제목</label><br/>
        <input type="text" name="title" id="title">
    </div>
    <div>
        <label for="body">본문</label><br/>
        <textarea name="body" id="body" cols="30" rows="10"></textarea> 
    </div>

    <input type="submit" value="글 생성하기">

</form>
```

#### form tag 
> - 메소드
>>  form data가 서버로 제출될 때 사용되는 HTTP 메소드를 명시한다.
>  - GET: 폼 데이터를 URL에 추가하여 전달
>>   - 브라우저에 캐시되어 저장 
>>    - 보안상 취약점 존재 
> - POST: 폼 데이터를 별도로 첨부하여 전달 
>>     GET 방식보다 보안성이 좋음 
>
>- 액션 
>>  폼 데이터를 서버로 보낼 때 해당 데이터가 도착할 url

#
#

## 입력한 글 DB에 저장하기 
-submit 타입의 input 태그를 입력하면  ```/create``` 로 이동하고, 여기서는 ```create.html```을 render하는 것이 아니라 새 글을 생성해주는 함수가 실행된다. 


```
from django.shortcuts import render, redirect
from .models import Blog
from django.utils import timezone

def create(request): # 블로그 글을 저장해주는 함수 --> 앞선 함수와 성격이 다르다 (무언가를 보여줄_render_필요가 없음)
    if(request.method=='POST'):
        post = Blog()                               # Blog 객체 생성 
        post.title = request.POST['title']          
        post.body = request.POST['body']
        post.tag = 0
        post.date = timezone.now()
        post.save()                                 # 데이터베이스에 저장하는 함수(```insertSQL```을 수행)

    return redirect('home') # 인자에 해당하는 URL로 HttpResponseRedirect 리턴 
```
#
> ### Redirect와 Render의 비교 
> render
> 요청한 페이지를 템플릿과 context를 결합하여 리턴 
> HttpResponse 객체를 리턴
> # 
> redirect 
> 특정한 Url로 요청을 보냄 

