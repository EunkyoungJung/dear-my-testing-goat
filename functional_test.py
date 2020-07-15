"""
<<기능 테스트>>
(1) 파이어폭스 브라우저 창을 실행하기 위해 셀레늄의 webdriver를 가동한다.
(2) 브라우저를 통해 로컬 PC상의 웹 페이지를 연다.
(3) 웹 페이지 타이틀에 "Django"라는 단어가 있는지 확인한다.

<<사용자 스토리 추가하기>>
(1) Marie는 멋진 작업 목록 온라인 앱이 나왔다는 소식을 듣고 해당 웹사이트를 확인하러 간다.
(2) 웹 페이지 타이틀과 헤더가 'To-Do'를 표시하고 있다.
(3) 그녀는 바로 작업을 추가하기로 한다.
(4) "공작깃털 사기"라고 테스트를 상자에 입력한다.
(5) 엔터키를 치면 페이지가 갱신되고 작업 목록에 "1: 공작깃털 사기" 아이템이 추가된다.
(6) 추가 아이템을 입력할 수 있는 여분의 텍스트 상자가 존재한다.
(7) 다시 "공작깃털을 이용해서 그물 만들기"라고 입력한다.
(8) 페이지는 다시 갱신되고, 두 개 아이템이 목록에 보인다.
(9) 사이트는 그녀를 위한 특정 URL을 생성해 준다.
(10) 이때 URL에 대한 설명도 함께 제공된다.
(11) 해당 URL에 접속하면 그녀가 만든 작업 목록이 그대로 있는 것을 확인할 수 있다.
(12) 만족하고 잠자리에 든다.
"""


from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

# webdriver.firefox()
# 위에처럼만 실행하면 "geckodriver" 에러가 발생
# webdriver manager를 추가로 설치해서 해결함
# 참고한 스택오버플로우: "https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path"





# (1) Marie는 멋진 작업 목록 온라인 앱이 나왔다는 소식을 듣고 해당 웹사이트를 확인하러 간다.
browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

# (2) 웹 페이지 타이틀과 헤더가 'To-Do'를 표시하고 있다.
browser.get('http://127.0.0.1:8000')
# assert 'Django' in browser.title, "Fail"
assert 'To-Do' in browser.title, "Fail: No such title in browser"

# (3) 그녀는 바로 작업을 추가하기로 한다.
# (4) "공작깃털 사기"라고 테스트를 상자에 입력한다.
# (5) 엔터키를 치면 페이지가 갱신되고 작업 목록에 "1: 공작깃털 사기" 아이템이 추가된다.
# (6) 추가 아이템을 입력할 수 있는 여분의 텍스트 상자가 존재한다.
# (7) 다시 "공작깃털을 이용해서 그물 만들기"라고 입력한다.
# (8) 페이지는 다시 갱신되고, 두 개 아이템이 목록에 보인다.
# (9) 사이트는 그녀를 위한 특정 URL을 생성해 준다.
# (10) 이때 URL에 대한 설명도 함께 제공된다.
# (11) 해당 URL에 접속하면 그녀가 만든 작업 목록이 그대로 있는 것을 확인할 수 있다.

# (12) 만족하고 잠자리에 든다.
browser.quit()