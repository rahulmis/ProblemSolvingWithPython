# arr = [0,1,1,2,3,5,8,13,21,34,55]

def fibusingrecursion(number):
    if(number<=0):
        print('Enter Grater Then 0 value : ')
    elif(number==1):
        return 0
    elif(number==2):
        return 1
    else:
        return fibusingrecursion(number-1)+fibusingrecursion(number-2)
for i in range(1,50):
    print(fibusingrecursion(i),end=' ')