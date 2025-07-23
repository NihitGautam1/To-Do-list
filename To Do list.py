print("📋 Welcome to Daily Task Organizer!\n")

print("Enter your tasks for the day (type 'done' to finish):")
tasks = []
while True:
    task = input("Task: ")
    if task.lower() == 'done':
        break
    tasks.append(task)

completed_tasks = []
incomplete_tasks = []

print("\nReview your tasks:")
for task in tasks:
    status = input(f"Did you complete '{task}'? (y/n): ").strip().lower()
    if status == 'y':
        completed_tasks.append(task)
    else:
        incomplete_tasks.append(task)

print("\n✅ Completed Tasks:")
for task in completed_tasks:
    print(f"- {task}")

print("\n❌ Incomplete Tasks:")
for task in incomplete_tasks:
    print(f"- {task}")
