# the goal of the game is to get to the sum of the cards of the number which is not over 21 
# if the sum of the cards is greater than 21 then it is bust and i loose immdiately 
# all cards from 2 to 10 count as face value 
# the king queen and jack count as 10 
# the ace can count as 1 or 11 as per the requirement it can take one value either 1 or 11 out of the two values 
# if the dealer ends its total under 17 then it must take out another card 

    # print(you)
bold = "\033[1m"# this is the escape sequence for making the text bolder
    # Reset ANSI escape sequence
reset = "\033[0m"
import os
# ---- here i am going to start the new black jack project
list_of_cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
# ---- above is the list made up of the cards
def black_jack(): 
    import random
    dealer=random.sample(list_of_cards,2)
    you=random.sample(list_of_cards,2)
    index_to_mask=random.randint(0,len(dealer)-1)
    print("sum of the cards of the dealer ",sum(dealer))
    original_value=dealer[index_to_mask]
    # sum_d=sum(dealer)
    # sum_y=sum(you)
    if sum(you)==21 or sum(dealer)>21:
        print(sum(you)," is the sum of the cards of the player <outside first>\n")
        print("you won the game at first strike")
        return
    elif sum(dealer)==21 or sum(you)>21:
        print(sum(you)," is the sum of the cards of the player <outside first>\n")
        print("dealer won the game at first strike")
        return
    elif sum(dealer)==sum(you):
        print(sum(you)," is the sum of the cards of the player <outside first>\n")
        print("it is a draw")
        return
    while True:
        if sum(dealer)<17:
            dealer.append(random.choice(list_of_cards))
        else:
            break
    print("NEW sum of the cards of the dealer ",sum(dealer))

    dealer[index_to_mask]="MASKED"
    # the above random.sample function returns a new list from the given sequence and the no of elements
    print(dealer)
    print(sum(you)," is the sum of the cards of the player <outside first>\n")
    
    print(you," the cards of the player")
    while True:
        print("\ndo you like to  bold + beat(b) + reset or bold + stand(s) + reset ")
        option=input()
        if option=="b":
            new_card=random.choice(list_of_cards)
            if new_card==11:
                print("you got an ACE\n")
                print("do you want it to use as \"1\" or \"11\"\n")
                if int(input())==1:
                    you.append(1)
                elif int(input())==11:
                    you.append(11)
            else:
                you.append(new_card)
            print(sum(you)," is the sum of the cards of the player <second>\n")
            if sum(you)>21:
                # print(sum(you)," is the sum of the cards of the player <inside the 21 condition>\n")
                print("the sum of the player is ",sum(you))
                print("you looose the sum exceeded 21")
                return 
        elif option=="s":
            break
        os.system('cls')
    dealer[index_to_mask]=original_value
    if sum(dealer)>sum(you) and sum(dealer)<=21:
        print("sum of the cards of the dealer ",sum(dealer))
        print("\n sum of the cards of the player ",sum(you))
        print("dealer is the WINNER")
    elif sum(dealer)<sum(you) and sum(you)<=21:
        print("sum of the cards of the dealer ",sum(dealer))
        print("\n sum of the cards of the player ",sum(you))
        print("you are the WINNER")
    elif sum(dealer)==sum(you) and (sum(dealer) and sum(you)<=21):
        print("sum of the cards of the dealer ",sum(dealer))
        print("\n sum of the cards of the dealer ",sum(you))
        print("It is a DRAW")
print(black_jack())
while True:
    print("do you want to play this game again")
    if input().lower()=="y":
        black_jack()
    else:
        break
    # sum_d=sum(dealer)
    # sum_y=sum(you)
    # if sum_d or sum_y >=21:

