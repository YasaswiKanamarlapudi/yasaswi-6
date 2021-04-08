n=int(input())
l=list(map(int,input().split()))
d={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten'}
v=['a','e','i','o','u']
f=0
cnt=0
for i in l:
    a=d[i]
    for j in a:
        if j in v:
            cnt=cnt+1
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if(l[i]+l[j]==cnt):
            f=f+1
print(d[f])
            
      
        
