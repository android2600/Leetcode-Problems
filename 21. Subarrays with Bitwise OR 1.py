def solve(B):
        count=0
        c_count=0
        flag=0
        for i in range(0,len(B)):
            '''
            sum_=0
            for j in range(i,len(B)):
                sum_=sum_|B[j] #carry forward
                if(sum_!=0):
                    count+=1
            '''
            if(B[i]==0 and flag==1):
                c_count+=1
            if(B[i]==0):
                count+=1
                flag=1
            if(flag==1 and B[i]==1):
                flag=0
                if(c_count!=0):
                    count=count+int((c_count-1)*c_count/2)
                c_count=0
        if(c_count!=0):
            count=count+c_count*2-1
        return int(len(B)*(len(B)+1)/2)-count
print(solve([ 1, 1, 0, 0, 1]))