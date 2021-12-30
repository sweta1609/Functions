import math
def checkMember(x):
    s = int (math.sqrt(x))
    return s*s == x

n=int(input())
result1=5*(n*n)+4
result2=5*(n*n)-4
if checkMember(result1) or checkMember(result2):
    print("true")
else:
    print("false")
