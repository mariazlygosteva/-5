day1 = int(input())
day2 = int(input())
day3 = int(input())

count = 0

if day1 == day2:
    count += 1
if day1 == day3:
    count += 1
if day2 == day3:
    count += 1

print(count)