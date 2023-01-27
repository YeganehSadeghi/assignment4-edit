#fibonachi series

a = int(input("enter a number ="))
n1  = 1
n2  = 1
sigma = 2 
counter = 1

print ("fibonachi seris = " , end = " ")
while(counter<= a):
    counter +=1
    print(n1, end=" ")
    n1=n2
    n2 = sigma 
    sigma = n1 + n2