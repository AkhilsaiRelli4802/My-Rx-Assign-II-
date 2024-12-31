# Given a sorted array of positive and negative numbers. You have to Square it and sort it. Constraint : Time complexity O(n) 
# Example: 
# Input: [-12, -8 , -7, -5, 2, 4, 5, 11, 15] 
# Output : [4, 16, 25, 25, 49, 56, 121, 144, 225] 

def sortarray(a):
    result=[]
    for i in a:
        i=i**2
        result.append(i)
    result.sort()
    return result
a=[-12, -8 , -7, -5, 2, 4, 5, 11, 15] 
res=sortarray(a)
print(res)
