# Given an array of Red Green Blue balls.You have to sort it. 
# Constraint : Time complexity O(n) 
# Constraint : Space complexity O(1) 
# Example: 
# Input: [R, G, B, G, G, R, B, B, G] 
# Output : [B,B,B,G,G,G,G,R, R] 


def ballssort(a):
    a.sort()
    return a
a=["R", "G", "B", "G", "G", "R", "B", "B", "G"] 
result= ballssort(a)
print(result)