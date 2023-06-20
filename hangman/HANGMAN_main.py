import os
import hangmann
import word_list
#first i created a string and made it to identate to check which character 
# of the given string is matching 
def main():
    print(hangmann.logo,"\n")
    # the_string_list=["ardvark","baboofg","cartede"]
    # the_empty_string=["_","_","_","_","_","_","_"]
    # import random 
    # chosen_word=random.choice(the_string_list)
    # # so now the problem is to clear all the empty string list with the letters 
    # length_of_the_string=len(the_empty_string)
    # flag="red"
    # length_=1
    # while length_<=length_of_the_string:
    #     guess_letter=input("guess a letter \n").lower()
    #     for x in chosen_word:
    #         if(x==guess_letter):
    #             the_empty_string[chosen_word.find(x)]=x
    #             flag="green"
    #     if flag=="green":
    #         print("\n you guessed the right letter")
    #     else:
    #         print("you guessed the wrong letter ")
    #     flag="red"
    #     length_+=1
    #     print(the_empty_string,"\n")
    # for i in the_empty_string:
    #     if i == '_':
    #         print("all attempts done \n you were not able to guess the full word")
    #         break
    # print("the full string guessed is ",the_empty_string)

    # ----------------------------------------------------
    # the following is the code which i made using the GPT modifcation of the for loop using the enumerate function  
    # ----------------------------------------------------
    # the_string_list = ["ardvark", "baboofg", "cartede"]
    import random
    chosen_word = random.choice(word_list.the_string_list)
    the_empty_string = ["_"for _ in chosen_word]
    # so now the problem is to clear all the empty string list with the letters
    length_of_the_string = len(the_empty_string)
    wrong_attempts=0
    flag = "red"
    length_ = 1
    while length_ <= length_of_the_string:
        guess_letter = input("guess a letter \n").lower()
        os.system('cls')
        for i, x in enumerate(chosen_word):
            if x == guess_letter:
                the_empty_string[i] = x
                flag = "green"
        if flag == "green":
            print("\n you guessed the right letter")
        else:
            print("you guessed the wrong letter\n")
            print("this was your %d wrong attempt"%(wrong_attempts+1))
            print(hangmann.hangman[wrong_attempts])
            wrong_attempts+=1
        flag = "red"
        length_ += 1
        print(the_empty_string, "\n")
        if '_' in the_empty_string:
            continue
        else:
            break 
    for i in the_empty_string:
        if i == '_':
            print("all attempts done \n\nyou were not able to guess the full word")
            print(hangmann.hangman[6])
            break
    print("\nthe full string guessed is ", the_empty_string)
    print("\nthe correct string was the ",chosen_word)


    # the following is the ascii ART drawing of the hangman 


    # then i made an empty string list and then replaces the empty characters of the list list with 
    # with the new character which is matching 
if __name__=='__main__':
    main()