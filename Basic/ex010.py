str1 = 'hello'
str2 = str1.upper()     # 원본은 바뀌지 않음
print(str1)
print(str2)

str3 = str2.lower()
print(str3)

str4 = "   HELLO   "    # 문자열은 별할수 없음, immutable sequence
str5 = str4.strip()     # 문자열 양옆 공백 제거, lstrip()-왼쪽공백제거, rstrip()-오른쪽 공백제거
print(str4)
print(str5)