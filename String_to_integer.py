class Solution:
    def myAtoi(self, s: str) -> int:
        num=""
        try:
            #if string is already an integer
            x=int(s)
            
            #check if it is within the bound limits given in ques
            if x<(-2)**31:
                return (-2)**31
            elif x>(2**31)-1:
                
                return (2**31)-1
            else:
                return x
        
        #if the string  has any other character /whitespace error will be catched
        except:
            
            try:
                
                #if first element a whitespace or - or + ,then skip
                if s[0]=="-" or " " or "+":
                    pass
                
                
                #else if it is an alphabet the else block will raise error,it will go to except block and out of code     
            
                else:
                    x=int(s[0])
                    
            except:
                
                return 0
        
        for i in range(len(s)):
            #if space bar after an integer then return the number or return 0
            try:
                x=int(s[i])
                num+=s[i]
            except:
                if s[i]==" ":
                    if num!="":
                        break
                    else:
                        continue
                elif (s[i]=="-" or "+") and num=="":
                    num+=s[i]
                else:
                    break
            
        try:
            x=int(num)
            if x<(-2)**31:
                return (-2)**31
            elif x>(2**31)-1:
                
                return (2**31)-1
            else:
                return x
        except:
            return 0
