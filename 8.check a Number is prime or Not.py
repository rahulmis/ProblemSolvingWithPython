"""
some prime numbers = 2,3,5,7,11,13,17.....
2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
"""
def checkprime(number):
    if(number>=2):
        for i in range(2,(number//2)+1):
            if(number%i==0):
                print('{} is not a Prime Number'.format(number))
                return
            else:
                pass
        print('{} is a Prime Number'.format(number))

    else:
        print('{} is not a Prime Number'.format(number))
checkprime(121)