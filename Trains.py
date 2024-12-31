def find_platforms(arr, dep):
    arr.sort()
    dep.sort()
    needed_platforms = 1  
    result = 1  
    i = 1  
    j = 0  
    while i < len(arr) and j < len(dep):
        if arr[i] <= dep[j]:
            needed_platforms += 1
            i += 1
        else:
            needed_platforms -= 1
            j += 1
        result = max(result, needed_platforms)    
    return result

arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]

print(find_platforms(arr, dep)) 
