import math

text = input("Enter a word or sentence: ")

length = len(text)
upper_text = text.upper() 
lower_text = text.lower() 
first_char = text[0]      

print("Length of text: " + str(length))
print("Uppercase: " + upper_text)
print("Lowercase: " + lower_text)
print("First character: " + first_char)

num = float(input("Enter a number: "))

square = num ** 2
square_root = math.sqrt(num) 
power_of_3 = math.pow(num, 3)
rounded = math.ceil(num) 

print("Square: " + str(square))
print("Square Root: " + str(square_root))
print("Power of 3: " + str(power_of_3))
print("Rounded up: " + str(rounded))
