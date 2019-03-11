#how many vowels in the string?
#how many digits in the string?
string = input()
vowelsCount = 0
digitsCount = 0
vowels = ["a", "e", "i", "o", "u"]
digits = str(list(range(10)))
for char in string: 
    if char in vowels:
        vowelsCount += 1
    elif char in digits:
        digitsCount += 1
        
print(vowelsCount)
print(digitsCount)