n=int(raw_input())
x=n
s=[]
min_array=[False]
min_array=n*min_array
while x!=0:
    s.append(int(raw_input()))
    x=x-1
#s.sort()


for i in range(0,n):
    if i==0:
        if s[i]<s[i+1]:
           min_array[i]=True
    elif i==n-1:
        if s[i]<s[i-1]:
            min_array[i]=True
    else:
        if (s[i]<s[i+1]) and (s[i]<s[i-1]):
            min_array[i]=True

candles=[1]
candles=n*candles
for i in range(0,n):
    if min_array[i]==True:
        for j in range(i-1,-1,-1):
            if min_array[j]==True:
                break
            if j==0:
                if s[j]>s[j+1]:
                    candles[j]=candles[j+1]+1
            else:
                if s[j]>s[j-1] and s[j]>s[j+1]:
                    candles[j]=max(candles[j-1],candles[j+1])+1
                elif s[j]>s[j-1]:
                    candles[j]=candles[j-1]+1
                elif s[j]>s[j+1]:
                    candles[j]=candles[j+1]+1


        for k in range(i+1,n):
            if min_array[k]==True:
                break
            if k==n-1:
                if s[k]>s[k-1]:
                    candles[k]=candles[k-1]+1
            else:
                if s[k]>s[k+1] or s[k]>s[k-1]:
                    candles[k]=max(candles[k-1],candles[k+1])+1
                elif s[k]>s[k-1]:
                    candles[k]=candles[k-1]+1
                elif s[k]>s[k+1]:
                    candles[k]=candles[k+1]+1


print sum(candles)


"""
        
    
    






w=s
w[0]=1
c=1
r=0
for i in range(1,x):
    if s[i]==s[i-1]:
        w[i]=1
    if s[i]>s[i-1]:
        w[i]=w[i-1]+1
for j in range(0,x):
    r=r+w[j]
    
print r
"""
