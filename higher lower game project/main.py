import art,dataa,random,os
score=0
print(art.logo)
cheqing_dict=[]
def random_generator_chequer():
    random_element=random.choice(dataa.data)
    for i in dataa.data:
        if random_element.values()==i.values():
            random_generator_chequer()
        else:
            cheqing_dict.append(random_element)
            return random_element

# so the above function was for generating the random element frpom the list
a=random_generator_chequer()
b=random_generator_chequer()
def display(a,b):
    print(a.values())
    print(art.vs)
    print(b.values())
def checker(a,b,score):
    # score=0
    # display(a,b)
    condition=True
    while condition:
        the_max=max(a["follower_count"],b["follower_count"])
        print("the score is inside the while loop",score)
        print("Who has more followers Type \"A\" or \"B\" ")
        the_chosen=input()
        if the_chosen=="A" and a["follower_count"]==the_max:
            # if a["follower_count"]==the_max:
            print("CORRECT")
            score+=1
            new_number=random_generator_chequer()
            os.system('cls')
            print("the score is ",score)
            display(a,new_number)
            # print("yes it is a recursive call returning ",checker(a,new_number,score))
            b=new_number
                # os.system('cls')
        elif the_chosen=="B" and b["follower_count"]==the_max:
            # if b["follower_count"]==the_max:
            print("CORRECT")
            score+=1
            new_number=random_generator_chequer()
            os.system('cls')
            # print("the score is ",score)
            display(b,new_number)
            # checker(b,new_number,score)

            """ this above commented calling of the function is done 
            because of the following reason-----

            The reason the print statement inside the while loop is 
            executed after the else block is because the checker function 
            is called recursively within the if and elif blocks. When the 
            user gives an incorrect answer, the innermost call to the 
            checker function will exit its while loop and return to the 
            previous call, which will then continue executing its while
              loop and print the prompt again.

            One way to fix this issue is to remove the recursive 
            calls to the checker function and instead use
             a loop to generate new numbers and update the values of a
               and b. This way, when the user gives an incorrect answer, 
               the while loop will exit and the game will end."""
            
            a=b
            b=new_number
        else:
            print("INCORRECT")
            # print("the score is ",score)
            condition=False
            # return score
            # print(f"your final score is {score}")
            # break
    return score
display(a,b)
score=checker(a,b,score)
print("your final score is ",score)

