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
