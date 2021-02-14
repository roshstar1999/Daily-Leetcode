#isBadVersion () API function predifined that returns whether an entered product no. is defect one or not(True or False)
#We are to find the first bad version in the list



class Solution:
    
    def firstBadVersion(self, n):
        
        #used binary search algorithm
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
