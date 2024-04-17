#Adding Task
def add_task(task_list,task):
    task_list.append(task)
    print("Task added Successfully")
    print()
    menu(task_list)

#display tasks
def show(task_list):
    index=1
    print("S.No    Tasks")
    for i in task_list:
        print(f"{index}. {i}")
        index+=1
    print("Task deleted Successfully")
    menu(task_list)

#delete tasks
def delete(task_list,inx):
    task_list.pop(inx-1)
    print("Task deleted Successfully")
    menu(task_list)

def menu(task_list):
    print("1.Add Task\n2.Delete Task\n3.Show Tasks")
    print("Enter your choice:")
    ch=int(input())
    if ch==1:
        print("Enter task to add:")
        task=input()
        add_task(task_list,task)
    elif ch==2:
        print("Enter the S.No to delete:")
        inx=int(input())
        delete(task_list,inx)
    elif ch==3:
        show(task_list)
    elif ch==4:
        exit()

#main
task_list=[]
menu(task_list)


       