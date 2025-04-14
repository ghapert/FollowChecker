# followers.txt 읽기
with open('followers.txt', 'r', encoding='utf-8') as f:
    followers = set(line.strip() for line in f if line.strip())

# followings.txt 읽기
with open('followings.txt', 'r', encoding='utf-8') as f:
    followings = set(line.strip() for line in f if line.strip())

# 나는 팔로우하지만, 나를 안팔로우하는 사람 찾기
not_following_back = followings - followers

# 결과 출력
print(f"나만 팔로우하는 사람 {len(not_following_back)}명:")
for user in sorted(not_following_back):
    print(user)

# 결과를 파일로 저장
with open('not_following_back.txt', 'w', encoding='utf-8') as f:
    for user in sorted(not_following_back):
        f.write(user + '\n')

print("not_following_back.txt 파일로 저장 완료")