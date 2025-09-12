list1 = [1, 2, [3, 4], 5] # mutable sequence 원본 수정 가능
print(list1)

element1 = list1[0]
print(element1)

element2 = list1[1]
print(element2 + 10)

element3 = list1[2]
print(element3)

element4 = list1[3]
print(element4)

list1[0] = 0
print(list1)

list2 = list1[2]
print(list2)
print(list2[1])

print(list1[2][0])
print(list1[2][1])

list3 = list1[1:3]
print(list3[0])

list_a = [273, 32, 103, "문자열", True, False]
print(list_a[-1])
print(list_a[-3])
print(list_a[-3][0])
print(list_a[1])
print(list_a[-4:-1])

