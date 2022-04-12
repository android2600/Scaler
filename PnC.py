class calculate:

    def factorial_recursion(self,num):
        if(num==1):
            return 1
        else:
            return num*(self.factorial_recursion(num-1))

    def factorial_iter(self,num):
        mult=1
        while(num>1):
            mult=mult*(num)
            num-=1
        return mult


class permutation (calculate):
    def solve_recursion(self,n,r):
        obj=calculate()
        N=obj.factorial_recursion(n)
        N_R=obj.factorial_recursion(n-r)
        print("n!= ",N)
        print("(n-r)!= ",N_R)
        return (N/N_R)

    def solve_iter(self,n,r):
        obj=calculate()
        N=obj.factorial_iter(n)
        N_R=obj.factorial_iter(n-r)
        print("n!= ",N)
        print("(n-r)!= ",N_R)
        return (N/N_R)

class combination:
    def solve_recursion(self,n,r):
        obj=calculate()
        N=obj.factorial_recursion(n)
        N_R=obj.factorial_recursion(n-r)
        R=obj.factorial_recursion(r)
        print("n!= ",N)
        print("(n-r)!= ",N_R)
        print("r!= ",R)
        return (N/(N_R*R))

    def solve_iter(self,n,r):
        obj=calculate()
        N=obj.factorial_iter(n)
        N_R=obj.factorial_iter(n-r)
        R=obj.factorial_iter(r)
        print("n!= ",N)
        print("(n-r)!= ",N_R)
        print("r!= ",R)
        return (N/(N_R*R))



result_p=permutation()
print(result_p.solve_recursion(5,2))
print(result_p.solve_iter(5,2))


result_c=combination()
print(result_c.solve_recursion(5,2))
print(result_c.solve_iter(5,2))