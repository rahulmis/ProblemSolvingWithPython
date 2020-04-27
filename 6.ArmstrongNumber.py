####### 153 is ArmStrong ?
# 153 = (1**3)+(5**3)+(3**3)
# 153 = 1 + + 125 + 27
# 153 = 153 It Is a Armstrong Number
####### 21 is ArmStrong ?
# 21 = (2**2)+(1**2)
# 21 = 5 It Is Not a Armstrong Number

def ArmStrong(n1):
    for i in range(1,n1+1):
        n = i
        s = str(n)
        cc = 0
        for i in range(len(s)):
            cc += int(s[i])**len(s)
        if(n==cc):
            print("The NUmber Is a ArmStrong Number {}".format(n))
        else:
            # print("The NUmber Is NOt a ArmStrong Number {}".format(n))
            pass


n1 = int(input("Enter The Number Your Want To Check Armstrong Or Not ?"))
res = ArmStrong(n1)