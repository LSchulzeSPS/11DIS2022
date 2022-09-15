values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
count = 0
numerals = ""
number = int(input("Please input a number between 1 and 3999: "))
if number >= 1 or number <= 3999:
    while number > 0:
        if number - values[count] >= 0:
            number -= values[count]
            numerals += roman[count]
        else:
            count += 1
else:
    print("Number out of parameters")
print(numerals)
