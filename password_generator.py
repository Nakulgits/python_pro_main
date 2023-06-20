import random
# here i am making a list of the letters to be used after wards
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','*','(',')']
print("welcome to password generator")
nr_letters=int(input("how many letters would you like in your password? \n"))
nr_symbols=int(input("how many symbols you would like in your password \n"))
nr_numbers=int(input("how many numbers you would like in your password \n"))

#----------------------------------------------
# this is the one way to do the same code 
#----------------------------------------------

# password_1=""
# password_2=""
# password_3=""
# count=0
# for char in range(nr_letters+1):
#     # random_char=random.choice(letters)
#     # password+=random_char
#     count+=1
#     password_1+=random.choice(letters)
#     print(password_1) 
# print(count)
# for char in range(nr_symbols+1):
#     password_2+=random.choice(symbols)
#     print(password_2)
# for char in range(nr_numbers+1):
#     password_3+=random.choice(numbers)
#     print(password_3)
# the_final_password=password_1+password_2+password_3
# print(the_final_password)
# # the above is the soft pass word code 

# # the below is the hard password code 
# # ----------------------------------------------
# password=""
# for char in the_final_password:
#     password+=random.choice(the_final_password)
# print("the final hard password is ",password)
# #-----------------------------------------------



#--------------------------------------
# this is the another way to do the same code
#---------------------------------------
elements_from_each_list=int(input("enter the no of elements to be taken from each list "))
result=""
for i in range(elements_from_each_list):
    result+=random.choice(letters)
    result+=random.choice(numbers)
    result+=random.choice(symbols)
result_final=""
for i in result:
    result_final+=random.choice(i)

print("the password the hard one is ",result_final)


