# enter todo
new_todo = input("Enter todo: ")
# add todo to array list
todos = []
todos.append(new_todo)
# show todo menu
menu_option = input("MENU\n1. Add Todo\n2. View Todos: ")
# check which menu item was selected
if menu_option == "1":
    # enter todo
    new_todo = input("Enter todo: ")
    # add todo to array list
    todos.append(new_todo)
    # show todo menu
    print("TODOS: ", todos)
elif menu_option == "2":
    # show todo menu
    print("TODOS: ", todos)
else:
    print("Invalid option")