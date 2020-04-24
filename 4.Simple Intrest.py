#si = p*t*r//100
"""
P = Principle amount
T = Time
R = Rate
"""
# bank > 100
# 100 ka 10%/month
# 5
# 50
def SimpleIntrest(p,r,t):
    return (p*t*r)/100


principle_amount = int(input("Enter Actual Amount : "))
rate = int(input("Enter percent  per month : "))
time = int(input("Enter  months : "))
res = SimpleIntrest(principle_amount,rate,time)
print('Simple Intrest = {}'.format(res))