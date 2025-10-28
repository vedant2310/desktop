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
    print("Top Five Salaries Will be",a[-5:][::-1])
elif c == 'bubble':
    bubble_sort(a)
    print("Sorted List is: ",a)
    print("Top Five Salaries Will be",a[-5:][::-1])
else:
    print("Error! Try Again")