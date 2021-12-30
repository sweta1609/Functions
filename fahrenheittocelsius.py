def printTable(start,end,step):
    pass
    c=0
    while start<=end:
        c=(start-32)*5/9
        print(start,int(c))
        start = start + step
    
start = int(input())
end = int(input())
step = int(input())
printTable(start,end,step)
