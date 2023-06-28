import os
import art
print(art.logo)
# os.system('cls')
print("welcome to the secret auction program")
the_dict={}
def auction(x):
    while True:
        print("what is your name \n")
        name=input()
        print("what is your bid \n")
        bid=int(input())
        x[name]=bid
        # print(x)
        print("Are there any other bidders \"yes\" or \"no\"?")
        answer=input()
        if answer =="y":
            os.system('cls')
            continue
        else:
            break 
    return x
# print(auction(the_dict))
# a=0
the_final_dict=auction(the_dict)
print("\n the final dict ",the_final_dict)
list_of_keys=list(the_final_dict.keys())
a=list_of_keys[0]
print("the chosen key ",a)
for i in the_final_dict:
    if the_final_dict[i]>the_final_dict[a]:
        a=i
print("the highest bid was ",a,"of the value ",the_final_dict[a])
    
    