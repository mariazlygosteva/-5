pin = input()

if len(pin) != 4 or not pin.isdigit():
    print("ERROR")
elif int(pin) in range(1900, 2051):
    print("ERROR")
elif len(set(pin)) != 4:
    print("ERROR")
else:
    print("OK")