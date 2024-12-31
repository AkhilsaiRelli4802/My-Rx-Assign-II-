# Sort hashmap by value. 
# Example: 
# Input: Map: {101=John Doe, 102=Jane Smith, 103=Peter Johnson} 
# output: Map: {102=Jane Smith, 101=John Doe, 103=Peter Johnson}

def sortmapbyvalue(a):
    sorteditems = sorted(a.items(), key=lambda item: item[1])  
    sortedmap = dict(sorteditems)  
    return sortedmap

a = {101: "John Doe", 102: "Jane Smith", 103: "Peter Johnson"}
result = sortmapbyvalue(a)

print(result)
