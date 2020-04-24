# 5! = 5*4*3*2*1 =
# 4! = 4*3*2*1 = 24
######################
# 5 = 1*2*3*4*5 =
#4 = 1*2*3*4 = 24
# 1! = 1 or 0! = 1
########################################
def factorial(no1):
    if(no1 == 0 or no1 ==1):
        return 1
    else:
        cc = 1
        for i in range(1,no1+1):
            cc = cc*i
        return cc
        # for i in range(no1,0,-1):
        #     cc = cc*i
        # return cc
llist = [1,2,3,4,5,6,7]
for i in range(1,21):
    # no1 = int(input("Enter Your Number : "))
    no1 = i
    res = factorial(no1)
    print("Factorial Of {} = {}".format(no1,res))