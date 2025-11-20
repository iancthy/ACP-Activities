num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum_result = num1 + num2
diff_result = num1 - num2
prod_result = num1 * num2
if num2 != 0:
    div_result = num1 / num2
else:
    div_result = "Error! Division by zero."

print("Addition: " + str(sum_result))
print("Subtraction: " + str(diff_result))
print("Multiplication: " + str(prod_result))
print("Division: " + str(div_result))
