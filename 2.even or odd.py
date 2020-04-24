def checkeven(no1):
    if(no1%2==0):
        return 1
    else:
        return 0

while True:
    no1 = int(input("Enter Your Number : "))
    res = checkeven(no1)
    if(res == 1):
        print("The {} is Even".format(no1))
    else:
        print("The {} is Odd".format(no1))

