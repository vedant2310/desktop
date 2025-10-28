call_queue = []

def addCall(customerID, calltime):
    call = {"Customer ID": customerID, "Call Time": calltime}
    call_queue.append(call)   # just append (don’t assign back)
    print(f"Customer ID {call['Customer ID']}, Call Time {call['Call Time']} mins")

def answerCall():
    if call_queue:
        call = call_queue.pop(0)   # remove first call (FIFO)
        print(f"Answering Call from Customer {call['Customer ID']}, Call time {call['Call Time']} mins")
    else:
        print("Error! Queue is empty.")

def viewQueue():
    if call_queue:
        print("Current Call Queue:")
        for i, call in enumerate(call_queue, 1):
            print(f"{i}. Customer {call['Customer ID']}, Call time {call['Call Time']} mins")
    else:
        print("Queue Empty")

def isQueueEmpty():
    if not call_queue:
        print("Queue is Empty")
    else:
        print("Queue is not empty")

def menu():
    while True: 
        print("\n^^^^^^ Call Center Services ^^^^^^^^")
        print("1. Add Call")
        print("2. Answer Call")
        print("3. View Queue")
        print("4. Check if Queue is Empty")
        print("5. Exit")

        choice = input("Enter your Choice: ")

        if choice == '1':
            customerID = int(input("Enter the Customer ID: "))
            calltime = int(input("Enter the call time (in mins): "))
            addCall(customerID, calltime)
        elif choice == '2':
            answerCall()
        elif choice == '3':
            viewQueue()
        elif choice == '4':
            isQueueEmpty()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Error! Invalid choice, try again.")

menu()


Algorithm for Call Center Queue Simulation

Step 1: Start
Step 2: Initialize an empty list call_queue to represent the queue.

Step 3: Define the following functions:

(a) addCall(customerID, callTime)

i.Create a dictionary with keys: "Customer ID" and "Call Time".

ii.Append it to call_queue.

iii.Display confirmation message.

(b) answerCall()

i.If the queue is not empty, remove the first call using pop(0) (FIFO).

ii.Display which call is being answered.

iii.Else, display “Queue is empty.”

(c) viewQueue()

i.If the queue is not empty, display all calls in order.

ii.Else, print “Queue Empty.”

(d) isQueueEmpty()

i.Check if call_queue is empty.

ii.Print the appropriate message.

Step 4: Create a menu-driven program:

Show choices:

1.Add Call

2.Answer Call

3.View Queue

4.Check if Queue is Empty

5.Exit

Perform the selected operation until the user chooses to exit.

Step 5: Stop
