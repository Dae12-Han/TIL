추가로 더 공부하고 싶을 시 ES6 이후 버전을 기준으로 보기

# 변수
+ 반드시 문자, '$', '_'로 시작
+ 대소문자 구분
+ 예약어 사용 X

## 변수 선언 키워드
### let
+ 블록 스코프를 갖는 지역 변수를 선언
+ 재할당 O
+ 재선언 X
+ ES6에서 추가
```
let number = 10 // 1.선언 및 초기값 할당
number = 20     // 2. 재할당
-----------------------------------------------
let number = 10 // 1.선언 및 초기값 할당
let number = 20 // 2.재선언 불가능
```
### const
+ 블록 스코프를 갖는 지역 변수를 선언
+ 재할당 X
+ 재선언 X
+ ES6에서 추가
```
const number = 10 // 1.선언 및 초기값 할당
number = 20       // 2. 재할당 불가능 -> 데이터 타입이 달라질 일이 없다!!
-----------------------------------------------
const number = 10 // 1.선언 및 초기값 할당
const number = 20 // 2.재선언 불가능
-----------------------------------------------
const number      // const declarations must be initialized
```
+ -> 대부분의 경우 const를 주로 쓰게 됌
### var

# 데이터 타입
## 원시 자료형
변수에 값이 직접 저장되는 자료형 (불변, 값이 복사)
+ Number
+ String
+ Boolean
+ null   
  - 변수의 값이 없음을 의도적으로 표현할 때 사용
  - null은 원시 자료형임에도 불구하고 Object로 출력된다!!
  - `typeof null  // "object"`
+ undefined
  - 변수 선언 이후 직접 값을 할당하지 않으면 자동으로 할당됨
  - `typeof undefined  // "undefined"`
## 참조 자료형
객체의 주소가 저장되는 자료형 (가변, 주소가 복사)
+ Objects (Object, Array, Function)

# DOM
## DOM 선택
### document.querySelector()
제공한 선택자와 일치하는 element 한 개 선택
### documnet.querySelectorAll()
제공한 선택자와 일치하는 여러 element 선택'

# 함수
## 화살표 함수 표현식
```
const arrow = function (name) {
  return `hello, ${name}`
}
```
```
// 1.function 키워드 삭제 후 화살표 작성
// 2.인자가 1개인 경우 () 생략 가능
// 3. 함수 본문이 return을 포함한 표현식이 1개일 경우 {} & return 삭제 가능
const arrow = name => `hello, ${name}`
```
# 참고
자바스크립트는 문장 마지막 세미콜론(;)을 선택적으로 사용 가능

# 이벤트
+ DOM에서 이벤트가 발생했을 때 생성되는 객체
+ DOM 요소는 event를 받고 받은 event를 '처리'할 수 있음 => event handler(이벤트 처리기)
## event handler
이벤트가 발생했을 때 실행되는 함수    
`.addEventListener()`  대표적인 이벤트 핸들러 중 하나    
#### `EventTarget.addEventListener(type, handler)`
대상에 특정 Event가 발생하면 지정한 이벤트를 받아 할 일을 등록한다.   
+ type -  수신할 이벤트 이름
+ handler - 발생한 이벤트 객체를 수신하는 콜백 함수
## 버블링
한 요소에 이벤트가 발생하면, 이 요소에 할당된 핸들러가 동작하고 이어서 부모 요소의 핸들러가 동작하는 현상
## 이벤트 기본 동작 취소
`.preventDefault()` 해당 이벤트에 대한 기본 동작을 실행하지 않도록 지정   
ex) copy 이벤트 동작 취소 -> 콘텐츠 무단 복사 방지
