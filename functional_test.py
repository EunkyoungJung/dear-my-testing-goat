"""
기능 테스트
* 파이어폭스 브라우저 창을 실행하기 위해 셀레늄의 webdriver를 가동한다.
* 브라우저를 통해 로컬 PC상의 웹 페이지를 연다.
* 웹 페이지 타이틀에 "Django"라는 단어가 있는지 확인한다.
"""


from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

# webdriver.firefox()
# 위에처럼만 실행하면 "geckodriver" 에러가 발생
# webdriver manager를 추가로 설치해서 해결함
# 참고한 스택오버플로우: "https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path"

browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
browser.get('http://127.0.0.1:8000')
assert 'Django' in browser.title
