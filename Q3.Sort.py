def selection_sort(array):
    for i in range(0, len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
def bubble_sort(array):
    for i in range (0,len(array)-1):
        for j in range (0,len(array)-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
n = int(input("Enter the Number of Salaries You want to enter: "))
a = []

for i in range(0, n):
    num = float(input(f"Salary NO.{i+1} will be: "))
    a.append(num)

print(f"Salary List Formed is: {a}")
c = input("Enter the Sorting Tecnique you want to use (selection/bubble): ")
if c == 'selection':
    selection_sort(a)
    print("Sorted List is: ",a)
    print("Top Salaries Will be",a[-5:][::-1])
elif c == 'bubble':
    bubble_sort(a)
    print("Sorted List is: ",a)
    print("Top Five Salaries Will be",a[-5:][::-1])
else:
    print("Error! Try Again")



Algorithm for Selection Sort

1.Start
2.Input the list of salaries.
3.For each position i in the list (from 0 to n–1):
4.Assume the element at i is the smallest.
5.Compare it with all remaining elements to the right.
6.If a smaller element is found, swap them.
7.Repeat until the entire list is sorted.
8.Display the sorted list and top 5 highest salaries.
9.Stop.

Algorithm for Bubble Sort
1.Start
2.Input the list of salaries.
3.Repeat (n–1) times:
4.For each pair of adjacent elements, compare them.
5.If the left element is greater than the right, swap them.
6.After all passes, the list becomes sorted in ascending order.
7.Display the sorted list and top 5 highest salaries.
8.Stop.