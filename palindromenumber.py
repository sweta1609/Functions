def checkPalindrome(num):
    rev=0
    z = num
    while(z>0):
        rev=rev*10+z%10
        z=z//10
    if(rev==num):
        print('true')
    else:
        print('false')
    
num = int(input())
checkPalindrome(num)
