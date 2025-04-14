# scrolling_followers.py

import pickle
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # 쿠키로 로그인
    with open('cookies.pkl', 'rb') as f:
        cookies = pickle.load(f)
    context.add_cookies(cookies)

    page.goto('https://www.instagram.com/')
    time.sleep(5)

    # 내 프로필로 이동
    page.goto('https://www.instagram.com/인스타아이디/')  # <-- 자신 인스타 ID로 수정
    time.sleep(5)

    # 팔로워 버튼 클릭
    page.click('a[href="/인스타아이디/followers/"]')  

    time.sleep(5)

    # 여기서 수동으로 쭉 스크롤 내려야함
    print("수동으로 팔로워 팝업 스크롤 쭉 내려주세요! (다 내리면 터미널에서 엔터)")
    input()

    # 수동 스크롤 끝나면 긁기
    popup = page.locator('div[role="dialog"]')
    followers = popup.locator('a[href^="/"]')  # ID만 긁어오기
    count = followers.count()

    print(f"총 {count}명 팔로워 찾음.")

    # 중복 없이 저장
    followers_set = set()
    for i in range(count):
        username = followers.nth(i).inner_text()
        followers_set.add(username)

    # 파일로 저장
    with open('followers.txt', 'w', encoding='utf-8') as f:
        for username in sorted(followers_set):
            f.write(username + '\n')

    print(f"followers.txt 파일에 저장 완료, 총 {len(followers_set)}명")
    browser.close()