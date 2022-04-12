class Bit:
    #def __init__(self,n) -> None:
    #    self.n=n
    #    pass
    #index is the index of bit from right
    def setBit(self,n,index):
        if((n>>index)%2==1):
            return n
        else:
            return n|1<<index
    
    def checkBit(self,n,index):
        if((n>>index)%2==1):
            return 1
        else:
            return 0
    
    def toggleBit(self,n,index):
        if((n>>index)%2==1):
            return n^1<<index
        else:
            return n|1<<index
    
    def clearBit(self,n,index):
        if((n>>index)%2==0):
            return n
        else:
            return n^1<<index
    
    def return_binary(self,n):
        binary=""
        while(n>0):
            binary=str(n%2)+binary
            n=n//2
        return binary

obj=Bit()
print(obj.return_binary(obj.setBit(11,0)))
