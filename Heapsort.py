def swap(A,i,j):
    A[i],A[j]=A[j],A[i]
"""
def siftDown(A,i,upper):
    while(True):
        l,r=i*2+1,i*2+2
        if max(l,r)<upper:
            if A[i]>=max(A[l],A[r]): break
            elif A[l]>A[r]:
                swap(A,i,l)
                i=l
            else:
                swap(A,i,r)
                i=r
        elif l<upper:
            if A[l]>A[i]:
                swap(A,i,l)
                i=l
            else:
                break
        elif r<upper:
            if A[r]>A[i]:
                swap(A,i,r)
                i=r
            else:
                break
        else:
            break
"""        
def siftDown(A,i,upper):
    largest=i
    l,r=2*i+1,2*i+2
    if(l<upper and A[largest]<A[l]):
        largest=l
    if(r<upper and A[largest]<A[r]):
        largest=r
    if(largest!=i):
        swap(A,i,largest)
        siftDown(A,largest,upper)

def  heapsort(A):
    for i in range(len(A)//2-1,-1,-1):
        siftDown(A,i,len(A))
    print(A)
    for i in range(len(A)-1,0,-1):
        swap(A,0,i)
        siftDown(A,0,i)

A=[5,16,8,14,20,1,26]
heapsort(A)
print(A)
