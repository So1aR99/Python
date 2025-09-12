print(str(123.456))
salary = input("연봉을 넣어주세요 ")
str_form1 = "컴퓨터 {0} 배워서 연봉 {1}만 원 되기".format("Python",salary) # {}안에 숫자로 순서 변경가능
str_form2 = f'연봉 {salary}만 원 되기'    # f-format
print(str_form1)
print(str_form2)

output_a = "{:d}".format(52)
output_b = "{:5d}".format(52)   # 5칸
output_c = "{:10d}".format(52)  # 10칸
output_d = "{:05d}".format(52)  # 양수
output_e = "{:05d}".format(-52) # 음수

print("# 기본")
print(output_a)
print("# 특정 칸에 출력하기")
print(output_b)
print(output_c)
print("# 빈칸을 0으로 채우기")
print(output_d)
print(output_e)