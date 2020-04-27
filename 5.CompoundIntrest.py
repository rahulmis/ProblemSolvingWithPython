# P = Principle amount
# T = Time
# R = Rate
#
# Compound interest (or compounding interest) is interest
# calculated on the initial principal,
# which also includes all of the accumulated interest
# of previous periods of a deposit or loan.
# Formula To Calculate Compound Intrest
#
# ci = (p*(1+(r/100))**t))

# create a function that will return Compound Intrest
def CompoundIntrest(p,t,r):
    return (p*(1+(r/100))**t)

# take p,r,t values from User
p = int(input("Enter Principle Amount : "))
r = int(input("Enter Rate : "))
t = int(input("Enter Time : "))
# Function call
res = CompoundIntrest(p,t,r)
print(res)
