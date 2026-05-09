def task():
    tasks=[]
    print("welcome to the task management app")

    total_task=int(input("enter how many task you want to add :-"))
    
    for i in range(1,total_task+1):
        taskname=input(f'enter taks{i}=') #enter taks 
        tasks.append(taskname)


    print(f"today taks are \n {tasks}")
    while True:
        operation=int(input(" 1-add\n2-update\n3-delete\n4-view\n5-exit/stop"))
        if operation==1:
            add=input("enter task you want to add= ")
            tasks.append(add)
            print(f"task{add} has been successully added...")
        elif operation==2:
            updated=input("Enter the task name your watn to update=")
            if updated in tasks:
                up=input("enter new taks")
                ind=tasks.index(updated)
                tasks[ind]=up
                print(f"task {up} updated")

        elif operation==3:
            del_val=input("which taks you want to delete")
            if del_val in tasks:
                ind=tasks.index(del_val)
                del tasks[ind]
                print(f"task {del_val} has been deleted")

        elif operation==4:
            print(tasks)





task()