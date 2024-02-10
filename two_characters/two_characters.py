def alternate(s):
    if len(s)<2:
        return 0
    ss = list(set(s))
    
    if len(s) == len(ss):
        return 2
        
    result = 0
    
    for i in range(len(ss)):
        for j in range(i+1,len(ss)):
            l =-1
            
            curr=0
            for k in range(len(s)):
                if s[k]==ss[i] or s[k]==ss[j]:
                    if l==-1 or l!=s[k]:
                        l = s[k]
                    else:
                        break
                    curr += 1
            else:
                result = max(result,curr)
    return result 