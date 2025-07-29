# Web
**World Wide Web**    
인터넷으로 연결된 컴퓨터들이 정보를 공부하는 거대한 정보 공간   
+ Web  
  사용자들이 정보를 검색하고 상호 작용하는 기술
+ Web site   
  인터넷에서 여러 개의 Web page가 모인 곳으로, 사용자들에게 정보나 서비스를 제공하는 공간
+ Web page   
  HTML, CSS 등의 웹 기술을 이용하여 만들어진, web site를 구성하는 하나의 요소
![web page 구성요소](/02_web/01_HTML_CSS/img/web%20page%20구성요소.png)
- <span style="color:darksalmon">HTML</span>        웹 사이트를 **정의**하고,
- <span style="color:deepskyblue">CSS</span>         **예쁘게** 꾸민 후에,
- <span style="color:gold">JavaScript</span>  **동작하게** 하는 것을 말합니다.
   
# HTML   
웹 페이지의 의미와 구조를 정의하는 언어       
Hyper Text Markup Language의 약자로서 웹 페이지를 만드는 언어    


웹 문서에서는 특정 텍스트에 Mark하기 위하여 HTML 태그(tag) 사용   
```html
<h1>제목</h1>
<p>내용이 들어올 자리입니다.</p>
<a href="http://www.naver.com">네이버로 이동</a>
```   
위 예시와 같이 제목과 같이 게 볼 수 있도록 하려면 `<h1>`태그 사용. 내용과 같은 글의 문단을 표시하려면 `<p>`태그 사용. 그리고 다른 웹 문서로 이동하기 위하여 `<a>` 태그 사용.

## HTML 구조
![html 구조](/02_web/01_HTML_CSS/img/html%20구조1.png)
![html 구조](/02_web/01_HTML_CSS/img/html%20구조2.png)

## HTML element/attribute
![html 요소](/02_web/01_HTML_CSS/img/html%20element.png)    
![html 속성](/02_web/01_HTML_CSS/img/html%20attribute.png)
### 속성 작성 규칙
1. 속성은 요소 이름과 속성 사이에 공백이 있어야함.
2. 하나 이상의 속성들이 있는 경우에는 속성 사이에 공백으로 구분.
3. 속성 값은 열고 닫는 따옴표로 감싸야 함.
### HTML 주석
+ 사용법 - `<!-- 메모내용 -->`  메모내용란에 메모할 문자 작성.