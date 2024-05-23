import os



def main():
    file_path = "todo_list.txt"
    tasks = load_task_from_file(file_path)
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
    elif choice =="2"
    

if _name_ == "_main_" :
    main()