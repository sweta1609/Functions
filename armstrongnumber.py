def armstrong(n):
    sum = 0
    order = len(str(n))
    m = n
    while (n>0):
        digit =n%10
        sum += digit**order
        n = n//10
    if(sum == m):
        print("true")
    else:
        print("false")
n = int(input())
armstrong(n)
