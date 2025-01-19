from datetime import datetime

class TodoList:
    def __init__(self):
        self.tasks = []

    def display_menu(self):
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

    def add_task(self):
        task_name = input("Enter the task: ").strip()
        if not task_name:
            print("Task cannot be empty.")
            return

        due_date_input = input("Enter the due date (YYYY-MM-DD) or leave blank for no due date: ").strip()
        due_date = None
        if due_date_input:
            try:
                due_date = datetime.strptime(due_date_input, "%Y-%m-%d").date()
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                return

        self.tasks.append({"task": task_name, "completed": False, "due_date": due_date})
        print(f"Task '{task_name}' added!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("\nYour Tasks:")
        for index, task in enumerate(self.tasks, start=1):
            status = "✔ Done" if task["completed"] else "✘ Pending"
            due_date = task["due_date"].strftime("%Y-%m-%d") if task["due_date"] else "No due date"
            print(f"{index}. {task['task']} - {status} (Due: {due_date})")

    def complete_task(self):
        self.view_tasks()
        if not self.tasks:
            return
        try:
            task_num = int(input("Enter the task number to mark as complete: "))
            if 1 <= task_num <= len(self.tasks):
                self.tasks[task_num - 1]["completed"] = True
                print(f"Task '{self.tasks[task_num - 1]['task']}' marked as completed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def delete_task(self):
        self.view_tasks()
        if not self.tasks:
            return
        try:
            task_num = int(input("Enter the task number to delete: "))
            if 1 <= task_num <= len(self.tasks):
                removed_task = self.tasks.pop(task_num - 1)
                print(f"Task '{removed_task['task']}' deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Choose an option: ").strip()
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.complete_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                print("Exiting Todo List. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    app = TodoList()
    app.run()
