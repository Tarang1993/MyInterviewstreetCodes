from sympy import sqrt

def factors(n):  
    fact=[1,n]  
    check=2  
    rootn=sqrt(n)  
    while check<rootn:  
        if n%check==0:  
            fact.append(check)  
            fact.append(n/check)  
        check+=1  
    if rootn==check:  
        fact.append(check)  
        fact.sort()  
    return fact

def main():
        
    S=raw_input()
    s=S.split()

    x=int(s[0])
    y=int(s[1])

    UN=raw_input()
    un_friendly=UN.split()
        
    fact=[]
    fact=factors(y)
    fact.sort()
    ans=0
    for i in fact:
        c=0
        for j in un_friendly:
            if int(j)%i==0:
                break
            else:
                c=c+1
        if c==x:
            ans=ans+1

    print ans

__name__=main()
