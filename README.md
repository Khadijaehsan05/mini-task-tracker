# Mini Task Tracker

This is my Assignment 2 mini project.

GitHub repo: https://github.com/Khadijaehsan05/mini-task-tracker

## What it does

It is a menu based task tracker made in Python. It saves tasks in a
JSON file, so the tasks are still there when I run the program again.

1. Add a task. It is saved as Pending.
2. View all tasks with Pending or Done.
3. Complete a task by its number.
4. Delete a task by its number.
5. Exit the program.

Each task is saved like this: {"title": "Read notes", "done": false}

## Files in this repo

- mini_task_tracker.py - the program
- README.md - this file

tasks.json is made by the program when a task is saved. I did not
upload it because it is made again when the program runs.

## How to run it in Google Colab

1. Upload mini_task_tracker.py to Colab.
2. Run it.
3. Use the menu to add and view tasks.
4. Run it again in the same Colab runtime and choose View to check
   that the saved tasks are still there.

Note: files in Colab are temporary. To keep tasks.json, download it
or save it to Google Drive.

## How to run it on my computer

I need Python 3. Nothing else to install.

```
python mini_task_tracker.py
```

## Sample run

```
--- TASK TRACKER ---
1. Add  2. View  3. Complete  4. Delete  5. Exit
Choice: 1
Task title: Read notes
Task added.
Choice: 2
1. Read notes [Pending]
Choice: 3
Task number: 1
Task completed.
Choice: 2
1. Read notes [Done]
Choice: 5
Goodbye!
```
