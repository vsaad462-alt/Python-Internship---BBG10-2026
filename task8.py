todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f"Added: '{task}'")

def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print(f"Removed: '{task}'")
    else:
        print(f"Task '{task}' not found!")

# Adding 5 tasks
add_task("Learn Python")
add_task("Complete Assignment")
add_task("Buy Groceries")
add_task("Go for a run")
add_task("Read a book")

print("\nCurrent Tasks:", todo_list)

# Removing 2 tasks
remove_task("Buy Groceries")
remove_task("Go for a run")

print("\nFinal Tasks:", todo_list)