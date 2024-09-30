# 금지어 목록
forbidden_words = ["세일", "판매", "특가", "할인"]

# 예시로 사용할 포스트 콘텐츠 리스트
post_contents = ["신상 초특가 세일 중", "질럿은 야마토 한방에 안죽어", "최신 게임 무료 다운 월정액 70%할인 중"]

# 금지어를 찾는 함수 정의
def find_forbidden_words(content):
    # 금지어가 발견된 위치(인덱스)를 저장할 리스트
    indices = []

    # 콘텐츠 문자열의 길이만큼 반복
    for i in range(len(content)):
        # 금지어 목록에서 각 금지어를 확인
        for word in forbidden_words:
            # 슬라이싱: 현재 위치 i부터 금지어의 길이만큼 잘라내어 비교
            # content[i : i + len(word)]는 i번째부터 금지어 길이만큼의 부분 문자열을 의미
            if content[i : i + len(word)] == word:
                # 금지어가 발견되면 금지어와 그 위치(i)를 튜플로 저장
                indices.append((word, i))

    # 발견된 금지어와 위치 정보가 담긴 리스트 반환
    return indices

# 각 콘텐츠에 대해 금지어 확인
for content in post_contents:
    # 금지어가 있는지 확인 후 그 결과를 indices에 저장
    indices = find_forbidden_words(content)
    
    # 콘텐츠 출력
    print(content)

    # 금지어가 발견되었을 때
    if indices:
        # 각 금지어와 그 위치를 출력
        for word, index in indices:
            # 금지어와 위치는 0부터 시작하므로 1을 더해 사용자에게 출력
            print(f"- \"{word}\" 금지어가 {index + 1}번째 글자에 등장하니 수정해주세요.")
    else:
        # 금지어가 없으면 성공 메시지 출력
        print("글이 성공적으로 등록되었습니다.")

    print()  # 줄바꿈