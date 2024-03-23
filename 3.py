num = int(input())

reversed_num = int(str(num)[::-1])

if reversed_num % 2 == 0:
    print("настоящее")
else:
    print("кривое")