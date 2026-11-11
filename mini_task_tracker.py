"""Mini Task Tracker — Week 1, Day 2.

A menu-based task tracker that stores tasks in tasks.json
and reloads the saved tasks when run again.

Each task is stored as {"title": "...", "done": False}.
Run with: python mini_task_tracker.py
"""

import json

TASKS_FILE = "tasks.json"


def load_tasks():
    """Load tasks from tasks.json, or start with an empty list."""
    try:
        with open(TASKS_FILE, "r") as file:
            tasks = json.load(file)
        # Only accept a list; anything else means start fresh.
        if isinstance(tasks, list):
            return tasks
        print("tasks.json is not a valid task list. Starting with an empty list.")
        return []
    except FileNotFoundError:
        # First run: no saved file yet, so begin with an empty list.
        return []
    except json.JSONDecodeError:
        print("tasks.json is damaged and could not be read. Starting with an empty list.")
        return []


def save_tasks(tasks):
    """Save the task list to tasks.json."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=2)


def add_task(tasks):
    """Ask for a task title and store it as Pending."""
    title = input("Task title: ").strip()
    if not title:
        print("Task title cannot be empty.")
        return
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added.")


def view_tasks(tasks):
    """Show a numbered task list with Pending or Done."""
    if not tasks:
        print("No tasks yet.")
        return
    for number, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Pending"
        print(f"{number}. {task['title']} [{status}]")


def _choose_task_number(tasks, action):
    """Ask for a task number and return its index, or None if invalid."""
    if not tasks:
        print("No tasks yet.")
        return None
    try:
        task_number = int(input("Task number: "))
    except ValueError:
        print("Invalid task number. Please enter a number.")
        return None
    if task_number < 1 or task_number > len(tasks):
        print(f"Invalid task number. Please enter a number between 1 and {len(tasks)}.")
        return None
    return task_number - 1


def complete_task(tasks):
    """Select a task number and mark its done field True."""
    index = _choose_task_number(tasks, "complete")
    if index is None:
        return
    if tasks[index]["done"]:
        print("That task is already completed.")
        return
    tasks[index]["done"] = True
    save_tasks(tasks)
    print("Task completed.")


def delete_task(tasks):
    """Select a task number and remove that task."""
    index = _choose_task_number(tasks, "delete")
    if index is None:
        return
    removed_task = tasks.pop(index)
    save_tasks(tasks)
    print(f"Task deleted: {removed_task['title']}")


def main():
    """Load saved tasks, then keep showing the menu until Exit."""
    tasks = load_tasks()

    while True:
        print("\n--- TASK TRACKER ---")
        print("1. Add  2. View  3. Complete  4. Delete  5. Exit")
        choice = input("Choice: ").strip()

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
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
