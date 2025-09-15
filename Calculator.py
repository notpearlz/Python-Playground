def main():

    start()




def start():
    print("Welcome to my calculator app")

    print("Please enter a math operation")

    operation = input()
    if(isValidOperation(operation)):
        print("Operation is valid")

    

def isValidOperation(operation):
    operationList = operation.split(' ')

    for x in operationList:
        print(x)
        
    return True


def add(num1, num2):
    pass

def subtract(num1, num2):
    pass

def divide(num1, num2):
    pass

def multiply(num1, num2):
    pass



main();
