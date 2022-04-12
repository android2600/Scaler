def binary_to_decimal(num):
    bin_num=0
    i=0
    while(num>0):
        bin_num+=(num%10)*1<<i
        i+=1
        num=num//10
    return bin_num
# bit manipulation
def grey_code(A):
    res=[]
    for i in range(1<<A):
        res.append(i^i>>1)
    return res
#print(binary_to_decimal(11001))
#print(grey_code(12))
