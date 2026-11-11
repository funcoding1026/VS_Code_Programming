# this program will resolve equation ax^2 + bx + c = 0
import math

def solve_quadratic(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return None, None
    
    elif delta == 0:
        x = -b / (2*a)
        return x, x
    
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return x1, x2

def main():
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    x1, x2 = solve_quadratic(a, b, c)
    if x1 is None:
        print("No real roots")
    else:
        print(f"x1 = {x1}, x2 = {x2}")

if __name__ == "__main__":
    main()
    
# this program will convert decimal to binary and vice versa
def decimal_to_binary(decimal):
    if decimal == 0:
        return "0"
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary

def binary_to_decimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal * 2 + int(digit)
    return decimal

def main():
    decimal = int(input("Enter a decimal number: "))
    binary = decimal_to_binary(decimal)
    print(f"{decimal} in binary is {binary}")

    binary_input = input("Enter a binary number: ")
    decimal_output = binary_to_decimal(binary_input)
    print(f"{binary_input} in decimal is {decimal_output}")

if __name__ == "__main__":
    main()
