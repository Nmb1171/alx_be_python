task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Provide a reminder based on priority and time sensitivity
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high-priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high-priority task. Complete it as soon as possible.")
    case "medium":
        print(f"Reminder: '{task}' is a medium-priority task. Try to complete it soon.")
    case "low":
        print(f"Note: '{task}' is a low-priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level entered.")
