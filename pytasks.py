print("Welcome To PyTasks.")
print('''
······························
:░█▀█░█░█░▀█▀░█▀█░█▀▀░█░█░█▀▀:
:░█▀▀░░█░░░█░░█▀█░▀▀█░█▀▄░▀▀█:
:░▀░░░░▀░░░▀░░▀░▀░▀▀▀░▀░▀░▀▀▀:
······························
      ''')
task = []
def show():
    print("1. add your tasks.")
    print("2. edit your tasks.")
    print("3. view your tasks.")
    print("4. delete your tasks.")
    
def ask():
    a = input("what you want to do?")
    if a == "1":
        add = input("add your tasks.")
        task.append(add)
    elif a == "2":
        edit_number = int(input("which task you want to change? , enter the index:"))
        edit_number = edit_number - 1
        edit = input("edit your task.")
        task[edit_number] = edit 
    elif a == "3":
        view = int(input("which task you want to view? , enter the index:"))
        view -= 1
        print(task[view])
    else:
        delete = int(input("which task you want to delete? , enter the index:"))
        delete -= 1
        del task[delete] 

end = ""
def main(): 
    global end
    while end != "yes":
        show()
        ask()
        end = input("do you want to quit?, type: yes or no")
        if end == "yes":
            break
        

main()
