# the_programming_dictionary={"bug":"an error in a program that prevents a program from running expectedly ",
#                             "function":"a piece of code that you can easily call over and over again",
#                             "loop":"the action of doing sometyhing over and over again "}

# print(the_programming_dictionary["bug"])
# the_programming_dictionary["new_key"]="new_ value"
# print(the_programming_dictionary)
# print(the_programming_dictionary["new_key"])

# # the following is the wiping out an existing dictionary 
# the_programming_dictionary={}
# print("\n")
# print(the_programming_dictionary)
# --------------------------------- above was just the basics of the dictionary


#----------------------- studemt scores to be converted to grades ----------------------------
# student_scores={
#     "harry":81,
#     "Ron":78,
#     "hermione":99,
#     "draco":74,
#     "Neville":62
# }
# student_grades={}
# # print(student_scores.keys())
# # print(student_scores.values())
# # print(student_scores.items())
# for i in student_scores:
#     if student_scores.get(i)>=91 and student_scores.get(i)<=100:
#         student_scores[i]="Outstanding"
#     elif student_scores.get(i)>=81 and student_scores.get(i)<=90:
#         student_scores[i]="Exceeds Expectations"
#     elif student_scores.get(i)>=71 and student_scores.get(i)<=80:
#         student_scores[i]="Acceptable"
#     else:
#         student_scores[i]="Fail"
# print(student_scores)

#------------------------------------------------------------------------------

# now i am going to make a nested dictionary inside a list -----------------------

# travel_log=[
#     {
#         "country":"france",
#         "visits":12,
#         "cities":["paris","lillie","Djon"]
#     },
#     {
#         "country":"germany",
#         "visits":"5",
#         "cities":["Berlin","hamburg","stuggart"]
#     }
# ]
# so above is list having dictionary as its elements 

#---------- this below code is working,the dictionary #---------- comprehension line is some what difficult to understand  
# def add_new_country(country,visits,list_of_cities,the_list):
#     keys=the_list[0].keys()
#     the_new_dict={"a":country,"b":visits,"c":list_of_cities}
#     the_final_dic={key:the_new_dict[value] for key,value in zip(keys,the_new_dict)}
#     the_list.append(the_final_dic)
#     print(the_list)




# -------- this is the new code and much better to understand 

# def add_new_country(country, visits, list_of_cities, the_list):
#     keys = the_list[0].keys()
#     the_new_dict = {"a": country, "b": visits, "c": list_of_cities}
#     the_final_dic = dict(zip(keys, the_new_dict.values()))
#     the_list.append(the_final_dic)
#     print(the_list)

# add_new_country("russia",12,["ab","cd","ef","gh"],travel_log)

# a={"A":"B","C":"D","E":"F"}
# b={"G":"H","I":"J","K":"L"}
a=["A","B","C"]
b=["D","E","F"]
z=dict(zip(a,b))
print(z)
# z[c]=["G","H","I"]
print(z)
