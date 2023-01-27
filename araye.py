import random

while True:
    
    list=[]
    for i in range(1,105):
        list.append (i)
    a = input("enter a random number between 1 and 100 = ")
    if a == 'f':
        break
    a = int(a)
    if a > 33:
        print("Erorr 404! :)")

    list1 = []

    for i in range(a):
        x = random.choice(list)
        list.remove(x)
        list1.append(x)
    print(list1)

    ans = input('finished = type f ')

