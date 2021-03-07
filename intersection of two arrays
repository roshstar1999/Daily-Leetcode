class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        x=[]
        map1={}
        map2={}
        
        for i in nums1:
        
            if i in map1:
                map1[i]+=1
            else:
                map1[i]=1
        
        
        for i in nums2:
        
            if i in map2:
                map2[i]+=1
            else:
                map2[i]=1
        
        if len(map1)<len(map2):
            for i in map1.keys():
                if i in map2:
                    if map1[i]==map2[i]:
                        for j in range(map1[i]):
                            x.append(i)
                    else:
                        dif=map1[i] if map1[i]<map2[i] else map2[i]
                        
                        for j in range(dif):
                            x.append(i)
        else:
            for i in map2.keys():
                if i in map1:
                    if map1[i]==map2[i]:
                        for j in range(map1[i]):
                            x.append(i)
                    else:
                        dif=map1[i] if map1[i]<map2[i] else map2[i]
                        
                        for j in range(dif):
                            x.append(i)
        return x
                    
                            
                
            
        
                
                
                    
                
                
                
                
                
                
                
                
                
        
