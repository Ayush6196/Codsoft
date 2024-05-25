import os



def save_task_to_file(file_path,tasks):
    with open(file_path, "w") as file:
        for task in tasks:
         file.write(f"{task}\n")

def load_tasks_from_file(file_path):
    task =  []
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            task = file.read().splitlines()
    return task



def main():
    file_path = "todo_list.txt"
    tasks = load_task_from_file(file_path)
    while True:
    print("\n=======To-Do-List=======")
    print("1.Show Tasks")
    print("2.Add Tasks")
    print("3.Update Tasks")
    print("4.Delete Tasks")
    print("5.Save and Exit")
    print("1.Show Tasks")
    choice = input("Enter your Choice(1-5): ")
    if choice =="1":
        show_tasks(tasks)
    elif choice =="2":
        new_task = ("Enter the task to add:")
        add_task(tasks,new_task)
    elif choice == "3":
        index = int(input("Enter the task index to input:"))
        updated_task = input("Enter the updated task:")
    elif choice == "4":
        index = int(input("Enter the task index to delete:"))
        delete_task(tasks,index)
    elif choice == "5":
        save_task_to_file(file_path,tasks)
        print("Task Saved. Exiting....")
        break
    else:
        print("Invalid Choice. Please try again.")
    

if _name_ == "_main_" :
    main()