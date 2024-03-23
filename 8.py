knuts = int(input("Введите количество кнатов: "))
galleons = knuts // (17 * 29)
sickles = (knuts % (17 * 29)) // 29
knuts2 = (knuts % (17 * 29)) % 29
if galleons:
    print(galleons, "галеонов")
if sickles:
    print(sickles, "сиклей")
if knuts2:
    print(knuts2, "кнатов")