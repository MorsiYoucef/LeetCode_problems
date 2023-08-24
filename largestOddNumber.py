def largestOddNumber(self, num):
        
        if int(num)%2!=0:
            return num
        else:
            s=0
            listof=[]
            for i in range(len(num)):
                if int(num[i])%2!=0:
                    s+=1
                
            if s==0:
                return ""
            else:
                k=1           
                char=""
                for char in num[::-1]:
                    if int(char)%2==0:
                        k+=1
                    else:
                        for i in range(len(num)-k+1):
                            listof.append(num[i])
                        return "".join(listof)
