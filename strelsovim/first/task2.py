x = input("")
list = []
count = 0
for i in range(length):
    list[i] = input("" + str(i+1) + " ").split("")
    if list[i] == []:
        count +=1
print("")
