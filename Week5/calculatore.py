def add(num1, num2):
	return num1 + num2

def sub(num1, num2):
	return num1 - num2

def mul(num1, num2):
	return num1 * num2

def div(num1, num2):
	return num1 / num2


print("====== Wel-Come To Simple Calculator ======")

while True:
    num1=int(input("Enter the 1st Number: "))
    num2=int(input("Enter the 2nd Number: "))
    operator=input("Enter the Operator(+,-,*,/): ")

    if operator == "+":
        print("Addition of : ", add(num1, num2))

    elif operator == "-":
        print("Subtraction of : ", sub(num1, num2))

    elif operator == "*":
        print("Multiplication of : ", mul(num1, num2))

    elif operator == "/":
        print("Division of : ", div(num1, num2))

    else:
        print("Invalid Operator for the calculation....!!") 

    print("---------------------------------------------------------")

    want_to_continue=input("Do U Want Continue? (y / n ) : ")
    if want_to_continue == 'n':
        break

    print("==========================================================")