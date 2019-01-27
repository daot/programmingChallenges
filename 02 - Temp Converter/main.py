to = int(input("To:\n1) Celsius\n2) Fahrenheit\n> "))
temp = int(input("# "))

if (to is 1):
    print((temp - 32) / 1.8, "*C")

if (to is 2):
    print((temp * 1.8) + 32, "*F")
