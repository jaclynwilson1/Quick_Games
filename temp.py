
lst = []

x = True

i = 0

while x == True:
    if i in lst:
        print("true")
    lst.append(i)
    print(lst)

    i = i+1

    if i == 10:
        x = False