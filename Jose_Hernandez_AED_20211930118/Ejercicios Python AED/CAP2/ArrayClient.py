import Array
maxSize = 10 
arr = Array.Array(maxSize) 
arr.insert(65) 
arr.insert(64)
arr.insert(56)
arr.insert(8)
arr.insert(74)
arr.insert(2)
arr.insert(4)
arr.insert(88)
arr.insert(9)
arr.insert(8)

m=arr.getMaxNum()
arr.traverse()
print("El máximo es:", m)

arr.deleteMaxNum()
print("Search for 555, returns", arr.search(555))


arr.traverse()
