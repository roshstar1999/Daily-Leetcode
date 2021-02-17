class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        h=head
        res=""
        while(h):
            res+=str(h.val)
            h=h.next
        num=0
        l=len(res)-1
        for i in range(len(res)):
            num+=int(res[l-i])*(2**i)
        return num
