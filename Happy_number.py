class Solution:
    def isHappy(self, n: int) -> bool:
        #to add sum of squares of digits using recursion
        def square_dig(k):
            if k==0:
                return 0
            return (k%10)**2+square_dig(k//10)
        
        k=n
        #for detecting endless loop collecting all new values collected in dic,if any new formed no. already has appeared,this means there is an endless loop=>return False
        while k!=1:
            k=square_dig(k)
            dic=[n]
            
            if k in dic:
                return False
            dic.append(k)
        #else True
        return True
