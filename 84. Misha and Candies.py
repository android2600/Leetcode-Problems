def solve(A, B):
    count=0
    heap=[]
    for i in range(len(A)):
        heap.append(A[i])
        n=len(heap)-1
        p=(n-1)//2
        parent=heap[p]
        current=heap[n]
        while n!=0 and parent>current:
            heap[p],heap[n]=heap[n],heap[p]
            n=p
            p=(n-1)//2
            parent=heap[p]
            current=heap[n]
    #return heap.pop()
    count=0
    while len(heap)>1 and heap[0]<=B:
        heap[len(heap)-1],heap[0]=heap[0],heap[len(heap)-1]
        temp=heap.pop()
        count+=temp//2
        current=0
        while ((2*current+2)<len(heap)) and (heap[2*current+1]<heap[current] or heap[2*current+2]<heap[current]):
            if heap[2*current+1]<heap[current] and heap[2*current+2]>heap[2*current+1]:
                heap[2*current+1],heap[current]=heap[current],heap[2*current+1]
                current=2*current+1
            elif heap[2*current+2]<heap[current]:
                heap[2*current+2],heap[current]=heap[current],heap[2*current+2]
                current=2*current+2
        if len(heap)==2:
            heap[0],heap[1]=min(heap[0],heap[1]),max(heap[0],heap[1])
        heap[0]+=(temp-temp//2)
        if len(heap)==2:
            heap[0],heap[1]=min(heap[0],heap[1]),max(heap[0],heap[1])
        current=0
        while ((2*current+2)<len(heap)) and (heap[2*current+1]<heap[current] or heap[2*current+2]<heap[current]):
            if heap[2*current+1]<heap[current] and heap[2*current+2]>heap[2*current+1]:
                heap[2*current+1],heap[current]=heap[current],heap[2*current+1]
                current=2*current+1
            elif heap[2*current+2]<heap[current]:
                heap[2*current+2],heap[current]=heap[current],heap[2*current+2]
                current=2*current+2
    return count

A = [ 324, 458, 481, 167, 939, 444, 388, 612, 943, 890, 953, 403, 653, 136, 168, 163, 186, 471 ]
B = 231
A = [ 440, 443, 463 ]
B = 810
#A=[ 110, 289, 585, 135, 314, 259, 238, 798, 954, 399, 492, 282, 311, 177, 804, 769, 191, 539, 830, 806, 854, 50, 373, 329, 549, 202, 399, 542, 166, 986, 446, 346, 58, 269, 103, 267, 547, 171, 713, 408, 847, 988, 704, 162, 850, 493, 59, 584, 588, 117, 639, 310, 615, 871, 977, 136, 973, 324, 450, 737, 778, 139, 606, 98, 968, 275, 911, 558, 849, 62, 495, 512, 106, 682, 980, 9, 517, 104, 80, 540, 689, 696, 396, 681, 541, 468, 12, 482, 459, 438, 924, 507, 725, 388, 579, 754, 421, 30, 151 ]
#B= 80
print(solve(A,B))