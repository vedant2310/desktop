def linear(array,key):
    for i in range (0,len(array)):
        if array[i] == key:
            print(f"Customer account ID:{key} Found at the index:{i} ")
            break
    else:
        print("Customer ID Not Found!")
def binary_search(array, key):
    start = 0
    end = len(array) - 1
    
    for i in range(start, len(array)):
        mid = int((start + end) / 2)
        
        if array[mid] == key:
            print(f"Customer Account ID: {key} has been found at the index {mid}")
            break
        
        if array[mid] < key:
            start = mid + 1
        
        if array[mid] > key:
            end = mid - 1
    
    else:
        print(f"Customer Account Id is not found")
n = int(input("Enter the Number of IDs: "))
a = []
print("NOTE: Put The IDs in Ascending or Descending order Only")
for i in range(0, n):
    num = int(input(f"Customer account ID No.{i+1} will be: "))
    a.append(num)

print(f"ID list formed is: {a}")
b = int(input("Enter The ID you want to find:"))
c = input("Enter the method through Which you want to find (linear or binary): ")
if c == 'linear':
    linear(a,b)
elif c == 'binary':
    binary_search(a,b)
else:
    print("Error! TRY AGAIN")