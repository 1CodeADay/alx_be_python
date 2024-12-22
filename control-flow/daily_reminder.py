# Define the function
def daily_reminder():
    # Prompt the user for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Match Case for priority level
    match priority:
        case 'high':
            priority_message = "high priority task"
        case 'medium':
            priority_message = "medium priority task"
        case 'low':
            priority_message = "low priority task"
        case _:
            priority_message = "task with an unknown priority"

    # Check if the task is time-bound
    if time_bound == 'yes':
        reminder_message = f"Reminder: '{task}' is a {priority_message} that requires immediate attention today!"
    else:
        reminder_message = f"Note: '{task}' is a {priority_message}. Consider completing it when you have free time."

    # Print the reminder message
    print(reminder_message)

# Run the function
daily_reminder()
