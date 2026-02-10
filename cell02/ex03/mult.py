#!python

a = float(input("Enter first number: \n"))
b = float(input("Enter second number: \n"))

result = a * b

print(f"{int(a)} x {int(b)} =", int(result))

if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")

