def happy_number(n):
    seen = set()
    while n!=1:
        if n in seen:
            return False # if loop detected
        seen.add(n)
        
        total = 0
        while n > 0:
            digit = n%10
            squared = digit*digit
            total+=squared
            n=n//10
        n=total
    return True

print(happy_number(82))

happy_number(n)
    
        
    
