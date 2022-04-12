
def solve(self, A):
    B=[[0]*len(A[0]) for i in range(0,len(A))]
    direction=1
    num=A[0]
    for k in range(0,A-2):
        top=k
        left=k
        right=A-k
        bottom=A-k
        if(direction==1):
            for i in range(left,right):
                B[top][left]=num
            direction=2
        
        if(direction==2):
            for i in range(top+1,bottom):
                B[i][right-1]=num
            direction=3
        
        if(direction==3):
            for i in range(right-2,left-1,-1):
                B[bottom-1][i]=num
            direction=4

        if(direction==4):
            for i in range(bottom-2,top,-1):
                B[i][top]=num
            direction=1

    #edge case len(A)=1,2,3
    return B
            