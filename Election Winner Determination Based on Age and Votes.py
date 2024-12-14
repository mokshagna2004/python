n = int(input())
vote =  list(map(int,input().split()))
age = list(map(int,input().split()))
c = [0]*max(vote)
for i in range(n):
    if age[i]>=18:
        c[vote[i]-1]+=1
m = max(c)
print(c.index(m)+1)
temp = c.sort(reverse = True)
if temp[0]==temp[1]:
    print(-1)
else:
    print(c.index(temp[0]+1))

            

  
