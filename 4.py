num = int(input())

if num % 10 == 1 and num != 11:
    print(num, "попугай")
elif 2 <= num % 10 <= 4 and not 12 <= num <= 14:
    print(num, "попугая")
else:
    print(num, "попугаев")