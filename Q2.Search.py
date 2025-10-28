def linear_search(array, key):
    for i in range(len(array)):
        if array[i] == key:
            print(f"Customer account ID {key} found at index {i}")
            break
    else:
        print("Customer ID not found!")

def binary_search(array, key):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        if array[mid] == key:
            print(f"Customer account ID {key} found at index {mid}")
            break
        elif array[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    else:
        print("Customer ID not found!")

# Main Program
n = int(input("Enter the number of IDs: "))
a = []
print("NOTE: Put The IDs in Ascending or Descending order Only")
for i in range(n):
    num = int(input(f"Customer account ID No.{i+1}: "))
    a.append(num)

print(f"ID list formed: {a}")
key = int(input("Enter the ID you want to find: "))
method = input("Enter search method (linear or binary): ").lower()

if method == 'linear':
    linear_search(a, key)
elif method == 'binary':
    binary_search(a, key)
else:
    print("Invalid choice! Please enter 'linear' or 'binary'.")



Algorithm for Linear Search
1.Start
2.Input list of customer IDs and the key to search.
3.Traverse the list from the first element to the last.
4.Compare each element with the key.
5.If a match is found, display the index and exit.
6.If the end of the list is reached and no match is found, display “Not Found.”
7.Stop.

Algorithm for Binary Search
1.Start
2.Input sorted list of customer IDs and the key to search.
3.Initialize start = 0 and end = n - 1.
4.Repeat while start <= end:
5.Calculate mid = (start + end) // 2.
6.If array[mid] == key, display index and exit.
7.Else if array[mid] < key, set start = mid + 1.
8.Else, set end = mid - 1.
9.If not found, display “Not Found.”
10.Stop.