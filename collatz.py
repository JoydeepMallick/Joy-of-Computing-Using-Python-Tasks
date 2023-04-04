def checkNum(num):
    iter = 1
    while(num != 1):
        if num%2 == 0:
            num//=2
        else:
            num = 3*num + 1
        iter+=1
    print("No. of iterations before reaching 1 : ",iter)

n = int(input("Enter a number : "))
checkNum(n)
