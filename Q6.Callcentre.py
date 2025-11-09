call_queue = []

def addCall(customerID,callTime):
  call = {"CustomerID":customerID,"Call Time":callTime}
  call_queue.append(call)
  print(f"Customer: {call['CustomerID']}, Talked for {call['Call Time']}")
  print("Added Successfully")

def answerCall():
  if not call_queue:
    print("No calls")
  else:
    call = call_queue.pop(0)
    print(f"Answering call from Customer: {call['CustomerID']}, Talked for {call['Call Time']}")
def view():
  if not call_queue:
    print("Empty")
  else:
    for i, call in enumerate(call_queue, 1):
            print(f"{i}. Customer ID {call['CustomerID']}, Call Time {call['Call Time']} mins")
def empty():
  if not call_queue:
    print("Nothing here man")
  else:
    print("queue is not empty")
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
            view()
        elif choice == '4':
            empty()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Error! Try again.")

menu()
