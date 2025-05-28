import json
import os
from datetime import datetime, timedelta

# 📂 FILE CONFIGURATION
# --------------------------------------------------
# This is the name of the JSON file used to store tasks
TASK_FILE = "tasks.json"

# 🧠 In-memory list to hold all current tasks
tasks = []

# 🔄 FUNCTION: Load Tasks from File
# --------------------------------------------------
def load_tasks():
    """
    Loads tasks from 'tasks.json' file, if available.
    ❗ Only keeps tasks created within the last 24 hours.
    📦 Stores the cleaned-up task list back to the file.
    """
    global tasks
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            try:
                raw_tasks = json.load(f)
                now = datetime.now()
                tasks = [
                    task for task in raw_tasks
                    if (now - datetime.fromisoformat(task["created_at"])) < timedelta(hours=24)
                ]
                save_tasks()
            except json.JSONDecodeError:
                tasks = []

# 💾 FUNCTION: Save Tasks to File
# --------------------------------------------------
def save_tasks():
    """
    Writes the current in-memory task list to 'tasks.json'.
    Ensures data is saved after any update.
    """
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# 🚀 MAIN PROGRAM LOOP
# --------------------------------------------------
def main():
    """
    Displays the main menu and handles user interactions.
    Users can:
    1️⃣ Add new tasks
    2️⃣ View all tasks
    3️⃣ Mark tasks as completed
    4️⃣ Delete tasks
    5️⃣ Exit the program
    """
    load_tasks()
    message = """
    -------------------------------
       🗂️ Task Manager - Main Menu
    -------------------------------
       1 - ➕ Add task 
       2 - 👀 View tasks 
       3 - ☑️ Mark task as done
       4 - 🗑️ Delete task
       5 - ❌ Exit
    """ 
    while True:
        print(message)
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task_as_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            save_tasks()
            print("👋 Exiting the task manager. See you soon!")
            break
        else:
            print("⚠️ Invalid choice. Please try again (1–5).")

# ➕ FUNCTION: Add New Task
# --------------------------------------------------
def add_task():
    """
    Prompts the user to enter a task description.
    Adds the task to the list with default status: not done.
    """
    task = input("Enter the task name: ").strip()
    if task:
        task_info = {
            "task": task,
            "status": False,
            "created_at": datetime.now().isoformat()
        }
        tasks.append(task_info)
        save_tasks()
        print("✅ Task added successfully!")
    else:
        print("⚠️ Task name cannot be empty.")

# 👀 FUNCTION: View All Tasks
# --------------------------------------------------
def view_tasks():
    """
    Displays all tasks with their index and status (done or not done).
    """
    if not tasks: 
        print("📭 No tasks found.")
        return

    print("\n📝 Your Tasks:")
    for i, task in enumerate(tasks): 
        status = "✅ Done" if task['status'] else "❌ Not Done"
        print(f"{i + 1}. {task['task']} - Status: {status}")
        print('-' * 40)

# ☑️ FUNCTION: Mark Task as Done
# --------------------------------------------------
def mark_task_as_done():
    """
    Lists incomplete tasks and lets the user mark one as completed.
    """
    incomplete_tasks = [task for task in tasks if not task['status']]
    if not incomplete_tasks:  
        print("🎉 All tasks are done. Great job!")
        return

    print("\n📌 Incomplete Tasks:")
    for i, task in enumerate(incomplete_tasks):
        print(f"{i + 1}. {task['task']}")
        print('-' * 20)

    try:
        task_number = int(input("Enter the task number to mark as done: "))
        if 1 <= task_number <= len(incomplete_tasks):
            index = tasks.index(incomplete_tasks[task_number - 1])
            tasks[index]['status'] = True
            save_tasks()
            print("✅ Task marked as done successfully!")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

# 🗑️ FUNCTION: Delete Task
# --------------------------------------------------
def delete_task():
    """
    Displays all tasks and allows the user to delete one by index.
    """
    if not tasks:
        print("📭 No tasks available to delete.")
        return

    print("\n🗑️ All Tasks:")
    for i, task in enumerate(tasks):
        status = "✅" if task['status'] else "❌"
        print(f"{i + 1}. {task['task']} - Status: {status}")
        print('-' * 20)

    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            deleted = tasks.pop(task_number - 1)
            save_tasks()
            print(f"🗑️ Task '{deleted['task']}' has been deleted.")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

# 🏁 START THE PROGRAM
main()
