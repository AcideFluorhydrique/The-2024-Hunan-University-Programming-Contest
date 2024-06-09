n,X = map(int, input().split())
C= input().split()
Current=[]
for i in C:
    Current.append(int(i))
Current.sort()
round=0
length=n-1
while True:
    if Current[0]>=X:
        round+=1
        break
    
    while Current[-1]>=X:
        Current.pop(-1)
        length-=1
    round+=1
    for i in range(length):
        Current[i]+=i+1
    Current[-1]+=n    
print(round)








