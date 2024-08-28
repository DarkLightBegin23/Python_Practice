secret_message = "i_n           ee        d_      y    o   u"
decoded = ""
for char in secret_message:
    if char != " ":  # 블랭크 아닐 때
        decoded += char  # 디코딩된 거에다가 char를 더해넣는당
print(decoded)