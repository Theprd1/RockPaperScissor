from art import logo
def add(n1, n2):
    return n1 + n2
# TODO 1: Write out the other 3 functions - subtract, multiply and divide.
def sub(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    if n2 == 0:
        return "Error: Division by zero"
    return n1 / n2
# TODO 2: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
operations={
    "+":add,
    "-":sub,
    "*":multiply,
    "/":divide
}
# TODO 3: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.
# print(operations['*'](4,8))
def calculator():
    print(logo)
    f_number=float(input("What is the First Number? :"))
    should_continue= True
    while should_continue:
        operation=input("Pick an Operation\n"
                            "+\n"
                            "-\n"
                            "*\n"
                         "/\n")
        s_number=float(input("What is the Second Number? :"))
        result=float(operations[operation](f_number, s_number))
        print(f"{f_number} {operation} {s_number} = {result}")
        response = input("Do you want to continue working with the previous result? Type 'yes' or 'no': ").lower()
        if response=="yes":
            f_number= result
        elif response=="no":
            should_continue = False
            print("\n"*20)
            calculator()
        else:
            print("Invalid input. Exiting.")
            should_continue = False

calculator()



