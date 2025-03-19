tasks=[]
while True:
  print("\nTO DO LIST")
  print("1.Add task")
  print("2.View tasks")
  print("3.Remove task")
  print("4.Exit task")
  choice=input("\nEnter the choice(1-4) : ")
  if choice=='1':
    task=input("Enter the task: ")
    tasks.append(task)
    print(f"{task} is added.")
  elif choice=='2':
    if not tasks:
      print("List is empty")
    else:
      print("\nTasks\n")
      for i,task in enumerate(tasks,1):
        print(f"{i}.{task}")
  elif choice=='3':
    if not tasks:
      print("No task to remove")
    else:
      try:
        task_number=int(input("\nEnter task number: "))
        if (1<=task_number<=len(tasks)):
          removed_task=tasks.pop(task_number-1)
          print(f"Removed task :{removed_task}")
        else:
          print("Invalid Number")
      except ValueError:
        print("Please enter a number ")
  elif choice=='4':
    print("Exiting...")
    break 
  else:
    print("Please enter between 1-4")
   
