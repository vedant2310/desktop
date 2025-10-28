class hashtable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def hashfunc(self, key):
        index = key % self.size
        return index

    def insert(self, key):
        I = self.hashfunc(key)
        c = I
        while self.table[I] is not None:
            if self.table[I] == key:
                print("\nError! Enter a Unique Element\n")
                return   # stop inserting duplicates
            else:
                print(f"\nCollision occurred at Index {I}, trying next index...\n")
                I = (I + 1) % self.size
                if c == I:   # we made a full loop
                    print("\nNo Empty Location Found! Hashtable is full.\n")
                    return
        self.table[I] = key
        print(f"\nElement {key} Inserted Successfully at Index {I}\n")

    def search(self, key):
        I = self.hashfunc(key)
        c = I
        probes = 0
        while self.table[I] != key:
            if self.table[I] is None:
                print("\nKey Not Found!\n")
                return
            I = (I + 1) % self.size
            probes += 1
            if c == I:
                print("\nKey Not Found!\n")
                return
        print(f"\n{key} is found at Index {I} (Probes: {probes})\n")

    def delete(self, key):
        I = self.hashfunc(key)
        c = I
        while self.table[I] != key:
            if self.table[I] is None:
                print("\nKey Not Found!\n")
                return
            I = (I + 1) % self.size
            if c == I:
                print("\nKey Not Found!\n")
                return
        self.table[I] = None
        print(f"\n{key} is deleted from Index: {I}\n")

    def display(self):
        for i in range(self.size):
            print(f"Index {i}: {self.table[i]}")

    def menu(self):
        print("\n=== Hash Table Menu ===")
        print("1. Insert Key")
        print("2. Search Key")
        print("3. Delete Key")
        print("4. Display Hashtable")
        print("0. Exit Menu")


hh = hashtable()
while True:
    hh.menu()
    choice = int(input("Enter your Choice: "))
    if choice == 1:
        a = int(input("Enter the Key: "))
        hh.insert(a)
    elif choice == 2:
        if hh.table == [None] * hh.size:
            print("\nThe Hashtable is Empty\n")
        else:
            b = int(input("Enter the key to be Searched: "))
            hh.search(b)
    elif choice == 3:
        if hh.table == [None] * hh.size:
            print("\nThe Hashtable is Empty\n")
        else:
            c = int(input("Enter the Key to be Deleted: "))
            hh.delete(c)
    elif choice == 4:
        hh.display()
    elif choice == 0:
        print("\nExiting....\n")
        break
    else:
        print("\nError! Invalid Choice.\n")



Algorithm: Hash Table Using Linear Probing

Start

Initialize hash table of fixed size (10) with all entries as None

Compute hash index as index = key % size (division method)

Insert(key):

-If index empty → store key

-Else use linear probing (index + 1) % size until empty slot found

Search(key):

-Compute index and check sequentially using linear probing until key found or empty slot reached

Delete(key):

-Locate key using same probing method and set that index to None

Display:

-Print all table indexes and their values

Repeat menu options (Insert, Search, Delete, Display) until user exits

Stop
