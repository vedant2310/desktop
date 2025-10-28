class TextEditor:
    def __init__(self):
        self.document = ""         # current document state
        self.undo_stack = []        # stack for undo actions
        self.redo_stack = []        # stack for redo actions

    def make_change(self, new_text):
        self.undo_stack.append(self.document)   # save current state before change
        self.document = new_text
        self.redo_stack.clear()                 # clear redo history after new change
        print(f"Change made: '{new_text}'")

    def undo(self):
        if not self.undo_stack:
            print("No actions to undo.")
        else:
            self.redo_stack.append(self.document)  # move current state to redo stack
            self.document = self.undo_stack.pop()  # restore last saved state
            print("Undo successful.")

    def redo(self):
        if not self.redo_stack:
            print("No actions to redo.")
        else:
            self.undo_stack.append(self.document)  # move current state to undo stack
            self.document = self.redo_stack.pop()  # reapply undone state
            print("Redo successful.")

    def display(self):
        print(f"\nCurrent Document State: '{self.document}'")


# ---------- Main Menu ----------
if __name__ == "__main__":
    editor = TextEditor()

    while True:
        print("\n=== TEXT EDITOR MENU ===")
        print("1. Make a Change")
        print("2. Undo Last Action")
        print("3. Redo Last Action")
        print("4. Display Document")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            text = input("Enter new text: ")
            editor.make_change(text)

        elif choice == '2':
            editor.undo()

        elif choice == '3':
            editor.redo()

        elif choice == '4':
            editor.display()

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please try again.")






"""Short Algorithm (10–12 lines)

Start

Initialize two stacks: Undo and Redo, and an empty string for the document.

Display menu with options: Make Change, Undo, Redo, Display, Exit.

For Make Change: push current state to Undo stack, update document, and clear Redo stack.

For Undo: if Undo stack not empty, push current document to Redo stack, pop from Undo to restore previous state.

For Redo: if Redo stack not empty, push current document to Undo stack, pop from Redo to restore undone change.

For Display: show current document state.

Repeat until the user chooses Exit.

Stop."""