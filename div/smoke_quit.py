#/usr/bin/env python

# statements with a # as first character are comments
# comments are ignored by the python interpreter (or, the computer if you like)


k = 100 # dummy variable
ak = 440; # smokes in january
smokes = ak # counter variable
S = smokes # number of smokes each month
r = 60 # reduction of smokes each month

m = k # count number of months

# while smoking, reduce number of smokes each month.
while smokes >= 0:
    smokes -= r
    if smokes >= 0:
        m += 1
        S += smokes

print(m, m - k, ak - (m - k)*r)
print(S)
