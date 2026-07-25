#TO-DO-LIST 

def show_menu():
    print("---TO DO List---")
    print("1. View Task ")
    print("2. Add Task")
    print("3. Mark as done")
    print("4. Delete task")
    print("5. Exit")

tasks=[]
def view_task():
    if not tasks:
        print("NO tasks found")
        return
    else:
        for i,task in enumerate(tasks,1):
            status = "✔️" if task['done'] else "X"
            print(f"{i}. {status} {task['name']}")

def add_task():
    name = input("Enter the task to be done: ")
    if name:
        tasks.append({"name": name, "done": False})
        print(f"Task added: {name}")
    else:
        print("Task can't be empty")

def marks_as_done():
    view_task()

    num=int(input("Mark task number as done: "))
    tasks[num-1]["done"] = True
    print(f"{tasks[num-1]['name']}: Marked as done")


def delete_task():
    view_task()

    num = int(input("Delete task number: "))
    removed = tasks.pop(num-1)
    print(f"{removed['name']}: Deleted")

def main():
    while True:
        show_menu()
        
        choice=int(input("Choose: "))
        if choice==1:
            view_task()
        elif choice==2:
            add_task()
        elif choice==3:
            marks_as_done()
        elif choice==4:
            delete_task()
        elif choice==5:
            print("Thanks for visiting.")
            print("Exiting...")
            break
main()