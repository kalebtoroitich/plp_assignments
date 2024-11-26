def add(num_1,num_2):
    result = num_1 + num_2
    return result

def subtraction(num_1,num_2):
    result = num_1 - num_2
    return result

def division(num_1,num_2):
    result = num_1 / num_2
    return result

def multiplication(num_1,num_2):
    result = num_1 * num_2
    return result

operations = {
    "+": add,
    "-": subtraction, 
    "*": multiplication,
    "/": division
}

num_1 = int(input("enter a number:"))
operation = input("enter a mathematical operation")
num_2 = int(input("enter the second number:"))

# calling the function according to the enterd key fron operations
if operation in operations:
    result = operations[operation](num_1, num_2)
    print(f"{num_1} {operation} {num_2} = {result}")
else:
    print("Invalid operation")
