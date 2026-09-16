def add(a: int, b: int) -> int:
    return a + b

def sub(a: int, b: int) -> int:
    return a - b

def mul(a: int, b: int) -> int:
    return a * b

def div(a: int, b: int) -> int:
    return a / b

def mod(a: int, b: int) -> int:
    return a % b

func_list = ["Add", "Sub", "Mul", "Div", "Mod"]

if __name__ == "__main__":
    print("Testing add Function: ")
    add_result = add(3,5)
    print("Addition result: ", add_result)

    print("Testing add Function: ")
    sub_result = sub(3,5)
    print("Subtraction result: ", sub_result)

    print("Testing add Function: ")
    mul_result = mul(3,5)
    print("Multiplication result: ", mul_result)

    print("Testing add Function: ")
    div_result = div(3,5)
    print("Division result: ", div_result)

    print("Testing add Function: ")
    mod_result = mod(3,5)
    print("Moduls result: ", mod_result)