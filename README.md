# iot-python-2026
IoT개발자 파이썬 리포지토리

- 문법 비교표

|이론개념|C/C++|Python|
|--------|-----|------|
|출력|print(), cout|`print()`|
|변수 선언|int a = 10;|`a = 10`|
|조건문|if (a > b) { ... }|`if a > b:`|
|반복문|for (int i = 0; i < 10; i++) { }|`for i in range(10):`|
|함수|int add(int a, int b) { }|`def add(a, b):`|
|배열|int arr[5]|`list`|
|문자/문자열|char, char[], char*, string|`str`|

- 장점

- 들여쓰기가 코드 블록, {} 불필요
- 선언이 없음
- 리스트가 배열보다 훨씬 편하고 간결
- 문자열 처리 간단
- 함수 만들기 간단


### 파이썬 설치

https://www.python.org/downloads/ - 다운로드
    최신 버전은 지양
    - 3.12페이지 검색해서 windows installer 64bit 클릭

    - ![alt text](image-2.png)




- documention만 체크 해제
- Advanced Options에서 install Python 3.12 for all users 활성화
- 콘솔에서 확인 안되면 add python.exe to PATH 체크가 안된것


### VS Code 확정
- 확장
    - Python으로 검색 후 설치
    ![alt text](image-1.png)

    -jupyter 검색 후 설치
    ![alt text](image-3.png)

    ### 파이썬 기본 학습
    1. 기본 입출력
        - .py 파일 작성
        - Ctrl +F5 파일 실행
        - 디버거 선택 >Python Debugger를 선택

    2. 리스트(배열 대체)
        - append ~ sort까지 11개 함수만 학습   

    3. 제어문

## 2일차

### 파일 입출력
인코딩 
    - EUC-KR:2바이트 한글 완성형 인코딩,cp949 동일한 의미
    - UTF-8: 1바이트 영문,3바이트 한글, 4바이트 이모지등 최대 4바이트 사용

- csv
    - 엑셀과 호화가능한 텍스트 팡리

- JSON: JavaScript Object Notation: 자바스크립트에서 데이터를 사용하기 위해 만든 표기 방법
- 딕셔너리를 텍스트화
- 데이터를 네트워크로 전달 할때 가장 효율적인 파일 형식
- XML을 대체하는 기술

### NoteBookLM 사용
 - notebooklm.google.com
 - 새로 만들기 클릭
 - 필요한 웹 사이트나 자료 업로드
  ![alt text](image-4.png)

  ## 3일차
  ### 파이썬 기본 학습
  - 라이브러리 사용 계속    
    - 타 언어의 경우 웹 검색, 다운로드, 개발위치 설치 혹은 복사
    - CPU 아키텍처에 따라 32bit(x86), 64bit마다 설치 방법이 상이하다
    - 파이썬은 자신만의 패키지 관리자(Package Manager: pip) 사용
    - 웹 검색 후 pip 명령어로 각 파이썬 개발 환경에 맞춰서 설치

    ''' bash
    pip install requests
    '''
    
    - 기타 자료 구조
        - 리스트 외 튜플, 딕셔너리,셋등...
        - 각 자료 구조 형태를 구분


- main
    - 파이썬은 main함수가 필요 없음
    - 여러 파일중 시작점을 지칭 할때는 사용
    - '__name__' 특수 변수를 사용

- 가상 환경
    - 프로젝트 마다 파이썬 환경을 따로 사용학시 위해 만들어진 개념
    - 프로젝트 생성시 독립도니 파이썬, 라이브러리 세트 새로 생성    
    - 일반적으로 프로젝트 폴더에서 생성

    - 파워 쉘 실행 정책 변경 필요(관리자 모드)

    ''' bash
        > Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
        > python -m venv iot-venv(가상환경이름)
    '''
    - 가상환경 생성 후 가상 환경 활성화 해야 함
    ![alt text](image-5.png)

    - 가상 환경은 github에 올리지 말것

    
- 객체 지향
    - c++의 객체 지향, 클래스와 동일
    - 접근 제한자가 없음(public,privated,protected)
    - C++과 달리 new 안씀, 변수등 선언 제약 사항이 많이 없음
    - 클래스 내의 모든 함수의 첫번째 파라미터는 `self`로 시작, c++의 this와 동일
    - 호출 시에는 



  ### 주피터 노트북
    - 파이썬을 좀더 인터렉티브하게 사용하고자 하는 취지
    - Project Jupyter
    - 확장에서 Jupyter 설치
    - 논문처럼 글과 소스 실행을 병행

    - 사용법
        - 명령 팔레트(Ctrl + Shift + P)
        ![alt text](image-6.png)
        - Untitled-1.ipynb 생성
        - 커널 선택 클릭
        - 마크다운 쉘(일반적 설명글), 코드쉘로 구분

    - 주피터 노트북 단축키
        - a: 현재 쉘위에 코드 쉘 추가
        - b: 현재 쉘 아래에 코드쉘 추가됨
        - enter: 현재 쉘 편집 모드로 진입
        - Ctrl + Enter: 마크 다운 쉘을 빠져 나오기, 코드 쉘을 실행
        ![alt text](image-7.png)

        -dd: 쉘 선택모드에서 쉘 삭제

        - 사용처
            - 웹상에서 동적하므로 많은 서비스를 지원
            - github codespace = 기존 리포지토리와 연결 지원