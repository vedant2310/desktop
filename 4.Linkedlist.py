class Student:
    def __init__(self, roll, name, marks):
        self.roll, self.name, self.marks, self.next = roll, name, marks, None

class LinkedList:
    def __init__(self):
        self.head = None

    def addStudent(self, roll, name, marks):
        s = Student(roll, name, marks)
        if not self.head:
            self.head = s
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = s
        print("Student Added")

    def updateStudent(self, roll, name=None, marks=None):
        cur = self.head
        while cur:
            if cur.roll == roll:
                if name: cur.name = name
                if marks is not None: cur.marks = marks
                print("Student Updated")
                return
            cur = cur.next
        print("Student Not Found")

    def searchStudent(self, roll):
        cur = self.head
        while cur:
            if cur.roll == roll:
                print(f"Found -> Roll: {cur.roll}, Name: {cur.name}, Marks: {cur.marks}")
                return
            cur = cur.next
        print("Student Not Found")

    def deleteStudent(self, roll):
        cur, prev = self.head, None
        while cur:
            if cur.roll == roll:
                if prev: prev.next = cur.next
                else: self.head = cur.next
                print("Student Deleted")
                return
            prev, cur = cur, cur.next
        print("Student Not Found")

    def display(self):
        cur = self.head
        if not cur:
            print("No Students")
            return
        print("\n--- Student List ---")
        while cur:
            print(f"Roll: {cur.roll}, Name: {cur.name}, Marks: {cur.marks}")
            cur = cur.next

# ---------- MENU ----------
ll = LinkedList()

while True:
    print("\n--- Student Management ---")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Display All")
    print("6. Exit")

    ch = input("Enter choice: ")

    if ch == '1':
        roll = int(input("Roll No: "))
        name = input("Name: ")
        marks = int(input("Marks: "))
        ll.addStudent(roll, name, marks)

    elif ch == '2':
        roll = int(input("Roll No to Update: "))
        name = input("New Name (Enter blank to skip): ").strip()
        marks = input("New Marks (Enter blank to skip): ").strip()
        ll.updateStudent(roll, name if name else None, int(marks) if marks else None)

    elif ch == '3':
        roll = int(input("Roll No to Search: "))
        ll.searchStudent(roll)

    elif ch == '4':
        roll = int(input("Roll No to Delete: "))
        ll.deleteStudent(roll)

    elif ch == '5':
        ll.display()

    elif ch == '6':
        print("Exiting...")
        break
    else:
        print("Invalid Choice")
s