def merge(Left,Right,A):
    nL=len(Left)
    nR=len(Right)
    i,j,k=0,0,0
    while(i<nL and j<nR):
        #print(int(str(Left[i])+str(Right[j]))>int(str(Right[j])+str(Left[i])),i,j,Left,Right)
        if(Left[i]>Right[j]):
            A[k]=Right[j]
            j=j+1
        else:
            A[k]=Left[i]
            i=i+1
        k=k+1
    while(i<nL):
        A[k]=Left[i]
        i+=1
        k+=1
    while(j<nR):
        A[k]=Right[j]
        j+=1
        k+=1

def mergesort(A):
    L=len(A)
    Left=A[:int(L/2)]
    Right=A[int(L/2):]
    if(L<2):
        return 
    else:    
        mergesort(Left)
        mergesort(Right)
        merge(Left,Right,A)
    print(A)

mergesort([2,5,3,4,8,7,18,16,42,14,0,34,9])


#int(str(Left[i])+str(Right[j]))>int(str(Right[i])+str(Left[j]))