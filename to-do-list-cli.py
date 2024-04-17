#Adding Task
def add_task(task_list,task):
    task_list.append(task)
    print("Task added Successfully.")
    print()
    menu(task_list)

#display tasks
def show(task_list):
    index=1
    if len(task_list)==0:
        print("Tasks list is empty.")
        print()
        menu(task_list)
    else:
        print("S.No Tasks")
        for i in task_list:
            print(f"{index}. {i}")
            index+=1
        print()
        menu(task_list)

#delete tasks
def delete(task_list,inx):
    task_list.pop(inx-1)
    print("Task deleted Successfully.")
    print()
    menu(task_list)

#close the program
def exit():
    print("Thank You")


def menu(task_list):
    print("Menu:")
    print("1.Add Task\n2.Delete Task\n3.Show Tasks\n4.Exit")
    print("Enter your choice:")
    ch=int(input())
    if ch==1:
        print("Enter task to add:")
        task=input()
        add_task(task_list,task)
    elif ch==2:
        if len(task_list)==0:
            print("Task list is empty")
            menu(task_list)
        else:
            print("Enter the S.No to delete:")
            inx=int(input())
            delete(task_list,inx)
    elif ch==3:
        show(task_list)
    elif ch==4:
        exit()

def main():
    task_list=[]
    menu(task_list)

if __name__=="__main__":
    main()


       
