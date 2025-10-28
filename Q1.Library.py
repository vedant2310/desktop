# Library Management System
# To manage and analyze book borrowing records

def compute_average(members):
    """Compute the average number of books borrowed by members."""
    total = sum(members)
    avg = total / len(members)
    return avg

def find_highest_lowest(books, borrow_counts):
    """Find the book with highest and lowest borrowings."""
    max_borrow = max(borrow_counts)
    min_borrow = min(borrow_counts)
    highest = books[borrow_counts.index(max_borrow)]
    lowest = books[borrow_counts.index(min_borrow)]
    return highest, lowest

def count_non_borrowers(members):
    """Count how many members borrowed 0 books."""
    return members.count(0)

def find_mode_book(books, borrow_counts):
    """Find the most frequently borrowed book (mode)."""
    freq = max(borrow_counts, key=borrow_counts.count)
    mode_book = books[borrow_counts.index(freq)]
    return mode_book

def main():
    # Sample data
    books = ["Book A", "Book B", "Book C", "Book D"]
    borrow_counts = [15, 23, 7, 23]   # times each book borrowed
    members = [3, 0, 2, 0, 5, 1]      # books borrowed by members

    while True:
        print("\n=== Library Borrowing System ===")
        print("1. Compute average borrowed books by members")
        print("2. Find highest and lowest borrowed book")
        print("3. Count members who borrowed 0 books")
        print("4. Display most frequently borrowed book")
        print("5. Exit")

        choice = int(input("Enter your choice (1-5): "))

        if choice == 1:
            avg = compute_average(members)
            print(f"\nAverage books borrowed by members: {avg:.2f}")

        elif choice == 2:
            highest, lowest = find_highest_lowest(books, borrow_counts)
            print(f"\nMost borrowed book: {highest}")
            print(f"Least borrowed book: {lowest}")

        elif choice == 3:
            non_borrowers = count_non_borrowers(members)
            print(f"\nNumber of members who borrowed 0 books: {non_borrowers}")

        elif choice == 4:
            mode_book = find_mode_book(books, borrow_counts)
            print(f"\nMost frequently borrowed book: {mode_book}")

        elif choice == 5:
            print("\nExiting program... Thank you!")
            break

        else:
            print("\nInvalid choice! Please enter a number between 1 and 5.")

# Run the program
main()




Algorithm: Library Borrowing System

Start

Initialize lists for books, borrow_counts, and members.

Display a menu with options for average, highest/lowest, non-borrowers, mode, and exit.

If user selects option 1, calculate average = sum(members) / total_members and display it.

If option 2, find maximum and minimum values in borrow_counts and display corresponding books.

If option 3, count members with borrow count = 0 and display the result.

If option 4, find the mode of borrow_counts and display the corresponding book.

If option 5, exit the program.

Display error message for invalid choices.

Repeat steps 3–9 until user exits.

Stop