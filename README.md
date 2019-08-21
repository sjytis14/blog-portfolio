#  Blog - Portfolio Project


## 프로젝트 소개

django를 이용하여 만든 blog 프로젝트이고, pythonanywhere를 통해 배포하였다.

## 기능

로그인, 로그아웃, 회원가입 기능을 추가하였고, 로그인 상태일때만 글쓰기 기능이 나타나도록 하였다.

## 장고 앱 구성

### blog

메인 화면

로그인 되어 있으면 new.html과 연결된 WRITE 버튼 활성화

### portfolio

등록된 static, media 파일과 게시물을 불러와 보여줌

### registration

로그인, 로그아웃, 회원 가입 기능

 - signup : 비밀번호 입력하고 한번 더 확인 후 가입
 - login : 이미 가입한 회원이면 로그인 후 메인 페이지로 이동, 아니면 로그인 화면에 머무름
 - logout : 로그아웃 후 로그아웃 성공 페이지로 이동


## 스크린샷

![Responsive image](https://cdn-class.likelion.org/media/submissions/QWpZ1vAcPZvVHOO.png)
