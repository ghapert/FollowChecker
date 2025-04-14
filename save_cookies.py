# save_cookies.py

import pickle
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # headless=False → 브라우저 띄워야 직접 로그인 가능
    context = browser.new_context()
    page = context.new_page()

    # 인스타그램 로그인 페이지 열기
    page.goto('https://www.instagram.com/accounts/login/')

    time.sleep(60)  
    # 60초 동안 수동 로그인 → 2단계 인증도 모두 완료해야함 

    # 로그인 완료 후 쿠키 저장
    cookies = context.cookies()
    with open("cookies.pkl", "wb") as f:
        pickle.dump(cookies, f)

    print("쿠키 저장 완료")
    browser.close()