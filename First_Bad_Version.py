class Solution:
    
    def firstBadVersion(self, n):
        left=1
        right=n
        
        while left!=right:
            mid=int((left+right)/2)
            
            if isBadVersion(mid):
                right=mid-1
                if not isBadVersion(right):
                    return mid
                
            else:
                left=mid+1
                if isBadVersion(left):
                    return left
        return right
