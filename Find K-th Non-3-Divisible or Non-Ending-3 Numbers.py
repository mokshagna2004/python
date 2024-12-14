n = int(input())
for i in range(n):
    
    k = int(input()) 
    count = 0
    i = 1
    while(1):
        if k%3 != 0 and k%10 != 3:
            count+=1
            if count == k:
                print(i)
                break
        i+=1
