queue = []
def add(event):
  queue.append(event)
  print("Event added successfully")
def nxt_event():
  if not queue:
    print("Nothing to process")
  else:
    nevent = queue.pop(0)
    print("Processing: ", nevent)
def display():
  if not queue:
    print("Queue is empty")
  else:
    for i, event in enumerate(queue):
      print(f"{i +1}  {event}")
def cancel(event_name):
  for i in range(len(queue)):
    if queue[i] == event_name:
      queue.remove(event_name)
      print("Removed {event_name}")
      return
  print("NOt found")

def menu():
  while True:


    print("1. Add")
    print("2. Process Next event")
    print("3. Display")
    print("4. Cancel an event")

    choice = int(input("Enter your choice: "))

    if choice == 1:

      event = input("Enter the event: ")
      add(event)

    elif choice == 2:

      nxt_event()

    elif choice == 3:

      display()

    elif choice == 4:
      c = input("Enter Event name to be deleted: ")
      cancel(c)

menu()
