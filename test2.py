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
    

