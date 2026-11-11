# this is a new program that i just created 
# this program allow us to print nbres from 0 to 4

def greet():
    print("this prog print nbres from 0 to 4")


greet()

c = 0
for i in range(5):
    c += 1
print(c)

# this program will convert celsius to fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is equal to {fahrenheit}°F")
