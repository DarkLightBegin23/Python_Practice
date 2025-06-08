def introduce_myself(name, age, man = True):
    print("저의 이름은 %s입니다." % name)  # 문자열 포매팅, 퍼센트(%) 포매팅
    print("나이는 %d세입니다." % age)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
        
introduce_myself("김한재", 25, True)
