# Mini Task Tracker
# Assignment 2
# Tasks are saved in tasks.json

import json


def load_tasks():
    # Load saved tasks, or start with an empty list if there is no file yet
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            return tasks
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    # Save the tasks to tasks.json
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=2)


def add_task(tasks):
    title = input("Task title: ").strip()
    if title == "":
        print("Task title cannot be empty.")
        return
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added.")


def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks yet.")
        return
    for i in range(len(tasks)):
        if tasks[i]["done"]:
            status = "Done"
        else:
            status = "Pending"
        print(str(i + 1) + ". " + tasks[i]["title"] + " [" + status + "]")


def complete_task(tasks):
    if len(tasks) == 0:
        print("No tasks yet.")
        return
    try:
        number = int(input("Task number: "))
    except ValueError:
        print("Invalid task number.")
        return
    if number < 1 or number > len(tasks):
        print("Invalid task number.")
        return
    tasks[number - 1]["done"] = True
    save_tasks(tasks)
    print("Task completed.")


def delete_task(tasks):
    if len(tasks) == 0:
        print("No tasks yet.")
        return
    try:
        number = int(input("Task number: "))
    except ValueError:
        print("Invalid task number.")
        return
    if number < 1 or number > len(tasks):
        print("Invalid task number.")
        return
    tasks.pop(number - 1)
    save_tasks(tasks)
    print("Task deleted.")


def main():
    tasks = load_tasks()

    while True:
        print("\n--- TASK TRACKER ---")
        print("1. Add  2. View  3. Complete  4. Delete  5. Exit")
        choice = input("Choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 to 5.")


main()
