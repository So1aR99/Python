numbers = [1,2,4,7,8,9,1,6,3,6,8,3,6,8,9,5,3,4]
counter = {} # empty dictionary

for number in numbers:
    counter[number] = numbers.count(number)

print(counter)