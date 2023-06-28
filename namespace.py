a=1
def change():
    global a
    a+=1
    print(f"the value of a in the function {a}")
    return a
print(change())
print(f"the value of a is {a}")