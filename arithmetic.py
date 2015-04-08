def add(num1, num2):
    return int(num1) + int(num2) 

def subtract(num1, num2):
    return int(num1) - int(num2)

def multiply(num1, num2):
    return int(num1) * int(num2)

def divide(num1, num2):
    return float(num1) / float(num2)

def square(num1):
    return int(num1)**2

def cube(num1):
    return int(num1)**3

def power(num1, num2):
    return int(num1)**int(num2)

def mod(num1, num2):
    return int(num1) % int(num2)

# def main():
#     # This is where the user can input the calculation.
#     input = raw_input()
#     numbers = input.split(' ')
#     # This will be a series of if statements for determining which function to call.
#     if input[0] == "+":
#         add(input[1], input[2])
#     elif input[0] == "-":
#         subtract(input[1], input[2])
#     elif input[0] == "*":
#         multiply(input[1], input[2])
#     elif input[0] == "/":
#         divide(input[1], input[2])
#     # elif input[0] == "-":
#     #     subtract()            

# if __name__ == '__main__':
#     main()