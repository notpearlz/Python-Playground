def main():

    calculator()




def calculator():
    print("Welcome to my calculator app")

    print("Please enter a simple math operation")
    print("Type 'x' to exit the app")

    while True:
        print('----------------------------------- \n\n\n')
        operation = input()

        if(operation == 'x'):
            break


        if(isValidOperation(operation)):
            operationList = operation.split(' ')

            num1 = int(operationList[0])
            operator = operationList[1]
            num2 = int(operationList[2])


            result = 0

            if(operator == '+'):
                result = add(num1,num2);
            elif(operator == '-'):
                result = subtract(num1,num2);
            elif(operator == '*'):
                result = multiply(num1,num2);
            elif(operator == '/'):
                result = divide(num1,num2);

            print(result);
        else:
            print("NOT A VALID EQUATION")


    


def isValidOperation(operation):
    operationList = operation.split(' ')

    if(len(operationList) == 3): 
       

        return True

    else:
        return False

        


def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def divide(num1, num2):
    return num1 / num2

def multiply(num1, num2):
    return num1 * num2



main();
