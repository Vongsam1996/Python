#To-do lists 
#defining task
def view_task(tasks):
    print("\nTo-do list")
    #including \nprint \n is Newline in String (Telling python to start a new line) 
    if not tasks:
        print("No tasks")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    print()
#This section of code is used to adjust the header label on "task" or "no task"
#enumerate(iterable, start=0)
#iterable: collection you want to loop over
#start: the starting value of the counter (default is 0)

def to_do_list(): 
    tasks = []

    while True:
        print("\nTo-do List")
        print("1. Add task")
        print("2. Remove task")
        print("3. View tasks")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            task_name = input("Enter the task name: ")
            tasks.append(task_name)
            print(f"Task '{task_name}' Added.")
        elif choice == '2':
            task_name = input("Enter the task name to remove: ")
            if task_name in tasks:
                tasks.remove(task_name)
                print(f"Task '{task_name}' Removed.")
            else:
                print(f"Task '{task_name}' Not Found.")
        elif choice == '3':
            view_task(tasks)
        elif choice == '4':
            print("Have A Great Day.")
            break
        else:
            print("Invalid choice. Please try again.")
#This section of code is used to adjust the header label on "task" or "no task"
to_do_list()