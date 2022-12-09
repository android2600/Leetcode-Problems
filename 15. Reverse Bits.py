def reverse(A):
        c=[]
        count=0
        while(A>0):
            if(A>1):
                c.append(A%2)
            else:
                c.append(1)
            if(A%2==1):
                count+=1
            A=int(A/2)
        #c.reverse()
        print(count)
        for i in range(0,32-len(c)):
            c.append(0)
        print(c)
        decimal=0
        for i in range(len(c)):
            decimal=decimal+c[i]*pow(2,len(c)-1-i)
        return decimal

print(reverse(490134411))