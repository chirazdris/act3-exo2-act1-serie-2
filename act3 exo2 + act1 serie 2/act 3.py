def conditional_replace(s, sub1, sub2, sub3, sub4):
    
    pos = s.find(sub1)
    if pos == -1:
        return s
    
    pos2 = s.find(sub2, pos+len(sub1))
    if pos2 == -1:
        return s.replace(sub1, sub4)
    
    else:
        if pos2 == pos+len(sub1):
            return s.replace(sub1, sub3)
        else:
           
            return s.replace(sub1, sub4)

result = conditional_replace("abc=fed","=","f","=e","=f")

print(result)