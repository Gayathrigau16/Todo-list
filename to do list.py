tasks = []

print("===========================To Do List===============================")
print("1.Add Task")
print("2.View Task")
print("3.Remove The Task")
print("4.Exit")

while True:
    choice = input("Enter Your Choice:")

    if choice == '1':
        task = input("Add Your Task:")
        tasks.append(task)
        print(".....Your Task Added.....")

    elif choice == '2':
        if len(tasks)==0:
            print("No Available Tasks")

        else:
            print("\nYour Task:")
            for i , t in enumerate(tasks ,start=1):
                print(f"{i}.{t}")

    elif choice == '3':
        if len(tasks)==0:
            print("No Tasks to Remove")

        else:
            for i,t in enumerate(tasks ,start=1):
                print(f"{i}.{t}")

                num = int(input("Enter the Remove choice:"))

                if 1 <=num <=len(tasks):
                    removed = tasks.pop(num-1)
                    print(f"{removed} removed")

                else:
                    print("Invalid choice")
                    
    elif choice == '4':
        print("Exiting..........")
        break

    else:
        print("Invalid choice")
