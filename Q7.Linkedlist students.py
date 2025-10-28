class Node:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
        self.prev = None
        self.next = None


class StudentRecordSystem:
    def __init__(self):
        self.head = None

    # Add a student record
    def addStudent(self, roll_no, name, marks):
        new_node = Node(roll_no, name, marks)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        print(f"Student added: Roll No: {roll_no}, Name: {name}, Marks: {marks}")

    # Delete a student record by roll number
    def deleteStudent(self, roll_no):
        if self.head is None:
            print("No records to delete.")
            return
        temp = self.head
        while temp:
            if temp.roll_no == roll_no:
                if temp.prev:
                    temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                if temp == self.head:
                    self.head = temp.next
                print(f"Record deleted for Roll No: {roll_no}")
                return
            temp = temp.next
        print(f"No student found with Roll No: {roll_no}")

    # Update student record
    def updateStudent(self, roll_no, new_name=None, new_marks=None):
        temp = self.head
        while temp:
            if temp.roll_no == roll_no:
                if new_name:
                    temp.name = new_name
                if new_marks is not None:
                    temp.marks = new_marks
                print(f"Record updated for Roll No: {roll_no}")
                return
            temp = temp.next
        print(f"No student found with Roll No: {roll_no}")

    # Search student by roll number
    def searchStudent(self, roll_no):
        temp = self.head
        while temp:
            if temp.roll_no == roll_no:
                print(f"Student Found → Roll No: {temp.roll_no}, Name: {temp.name}, Marks: {temp.marks}")
                return
            temp = temp.next
        print(f"No student found with Roll No: {roll_no}")

    # Sort records by marks or roll number
    def sortRecords(self, key="marks", ascending=True):
        if self.head is None:
            print("No records to sort.")
            return

        swapped = True
        while swapped:
            swapped = False
            temp = self.head
            while temp.next:
                first = temp
                second = temp.next
                if key == "marks":
                    condition = (first.marks > second.marks) if ascending else (first.marks < second.marks)
                else:  # key == "roll_no"
                    condition = (first.roll_no > second.roll_no) if ascending else (first.roll_no < second.roll_no)

                if condition:
                    first.roll_no, second.roll_no = second.roll_no, first.roll_no
                    first.name, second.name = second.name, first.name
                    first.marks, second.marks = second.marks, first.marks
                    swapped = True
                temp = temp.next
        print(f"Records sorted by {key} in {'ascending' if ascending else 'descending'} order.")

    # Display all records
    def displayRecords(self):
        if self.head is None:
            print("No records to display.")
            return
        temp = self.head
        print("\n--- Student Records ---")
        while temp:
            print(f"Roll No: {temp.roll_no}, Name: {temp.name}, Marks: {temp.marks}")
            temp = temp.next
        print("------------------------")


# -------- Main Program --------
system = StudentRecordSystem()

while True:
    print("\n=== Student Record Management System ===")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Update Student")
    print("4. Search Student")
    print("5. Sort Records")
    print("6. Display All Records")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
        system.addStudent(roll, name, marks)

    elif choice == '2':
        roll = int(input("Enter Roll No to delete: "))
        system.deleteStudent(roll)

    elif choice == '3':
        roll = int(input("Enter Roll No to update: "))
        new_name = input("Enter new Name (press Enter to skip): ")
        marks_input = input("Enter new Marks (press Enter to skip): ")
        new_marks = float(marks_input) if marks_input else None
        system.updateStudent(roll, new_name if new_name else None, new_marks)

    elif choice == '4':
        roll = int(input("Enter Roll No to search: "))
        system.searchStudent(roll)

    elif choice == '5':
        key = input("Sort by (marks/roll_no): ").strip().lower()
        order = input("Order (asc/desc): ").strip().lower()
        system.sortRecords(key, ascending=(order == 'asc'))

    elif choice == '6':
        system.displayRecords()

    elif choice == '7':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")



Algorithm: Student Record Management System

Start the program.

Create a linked list node with Roll No, Name, Marks, and link pointers.

Initialize the head of the list as None.

To Add Student, create a new node and link it at the end.

To Delete Student, search by roll number and adjust links to remove the node.

To Update Student, search the node and modify name or marks.

To Search Student, traverse the list to find the given roll number.

To Sort Records, compare and swap nodes based on roll number or marks.

To Display Records, traverse and print all student details.

Repeat menu options until the user chooses Exit.

Stop the program.