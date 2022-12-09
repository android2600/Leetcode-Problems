def solve(A):
        x=A
        last_bit=0
        result=0
        while(x>0):
            x=x>>1        
            last_bit+=1
        for i in range(0,last_bit):
            result+=(A%2)*5**(i+1)
            print((A%2)*5**(i+1))
            A=A//2

        return result

func=solve(10)
print(func)