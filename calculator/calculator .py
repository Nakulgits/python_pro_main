# first i am making the basic functions 
def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2
dicte={add:"+",subtract:"-",multiply:"*",divide:"/"}
dictt=dict(zip(dicte.values(),dicte.keys()))
# print(dictt)
# while True:
import art
print(art.logo)
def Calculator():
    num1=int(input("what is the first numnber \n").round())
    for symbol in dictt:
        print(symbol)
    operation_symbol=input("what opeartion to be done ")
    num2=float(input("what is the second numnber \n").round())
    calculation_function=dictt[operation_symbol]
    answer=calculation_function(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    while True:
        print(f"do you want to do another operation on the result {answer} or want to start a new calculation")
        reponse=input("""press \"no\" for ending the calculation or \"n\" for starting the new calculation
        or type anything for continuing the calculation""").lower()
        if reponse=="no":
            break
        elif reponse=="n":
            Calculator()
        operation_symbol=input("what opeartion to be done ")
        num2=int(input("what is the next numnber \n"))
        calculation_function=dictt[operation_symbol]
        new_result=calculation_function(answer,num2)
        print(f"{answer} {operation_symbol} {num2} = {new_result}")   
        answer=new_result
Calculator()
# print("\n",answer)