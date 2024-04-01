# file = open('todos.txt','r')
# todos = file.readlines()
# file.close()
from module.function import get_todos

while True:
    user_action = input("Type add , edit, show, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add") or user_action.startswith("new"):
        todo = user_action[4:]
        todos = get_todos()

        todos.append(todo)
        # file = open('todos.txt','w')
        # file.writelines(todos)
        # file.close()
        todos.append(todo + '\n')

        with open('todos.txt','w') as file:
            file.writelines(todos)

    elif user_action.startswith("show"):

        todos = get_todos()

        for index,item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = user_action[5:]
            pos = int(number) - 1

            todos = get_todos()

            new_todo = input("Enter new to do : ")
            todos[pos] = new_todo + "\n"

            with open('todos.txt','w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid")
            continue
    elif user_action.startswith("complete"):
        try:
            com_num = int(user_action[9:])
            todos = get_todos()
            index = com_num - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was remove from the list"
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print('Command is not valid')
print("Bye")


