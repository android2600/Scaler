def swap(A,x,y):
    temp=A[x]
    A[x]=A[y]
    A[y]=temp

def partition(A,start,end):
    pivot_value=A[end]
    p_index=start

    for i in range(start,end):
        if(A[i]<=pivot_value):
            swap(A,i,p_index)
            p_index+=1
    swap(A,p_index,end)
    return p_index

def quicksort(A,start,end):
    if(start<end):
        p_index=partition(A,start,end)
        quicksort(A,p_index+1,end)
        quicksort(A,start,p_index-1)
    return(A)

A=[2,5,3,4,8,7,1,1,4,4,0,-1,9]
print(quicksort(A,0,len(A)-1))
