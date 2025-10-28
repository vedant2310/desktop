from collections import deque

class EventQueue:
    def __init__(self):
        self.queue = deque()

    def add_event(self, event):
        self.queue.append(event)
        print(f"Event '{event}' added to queue.")

    def process_event(self):
        if not self.queue:
            print("No events to process.")
        else:
            event = self.queue.popleft()
            print(f"Processing event: {event}")

    def display_events(self):
        if not self.queue:
            print("No pending events.")
        else:
            print("Pending Events in Queue:")
            for e in self.queue:
                print("→", e)

    def cancel_event(self, event):
        if event in self.queue:
            self.queue.remove(event)
            print(f"Event '{event}' canceled successfully.")
        else:
            print("Event not found or already processed.")

# ---------- Main Menu ----------
if __name__ == "__main__":
    eq = EventQueue()

    while True:
        print("\n=== EVENT PROCESSING SYSTEM ===")
        print("1. Add Event")
        print("2. Process Next Event")
        print("3. Display Pending Events")
        print("4. Cancel an Event")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            event = input("Enter Event Name: ")
            eq.add_event(event)

        elif choice == '2':
            eq.process_event()

        elif choice == '3':
            eq.display_events()

        elif choice == '4':
            event = input("Enter Event Name to Cancel: ")
            eq.cancel_event(event)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please try again.")





"""Short Algorithm (10–12 lines)

Start

Initialize an empty queue using deque().

Display a menu with options to Add, Process, Display, Cancel, or Exit.

If the user chooses Add, append the event to the queue.

If Process, remove and display the first event from the queue.

If Display, show all events currently in the queue.

If Cancel, remove the specified event from the queue if it exists.

If Exit, terminate the program.

For invalid inputs, display an error message.

Repeat steps 3–9 until user exits.

Stop."""