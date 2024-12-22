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

    # Construct reminder message based on time sensitivity
    if time_bound == 'yes':
        action_message = "that requires immediate attention today!"
    else:
        action_message = "Consider completing it when you have free time."

    # Combine both priority and time sensitivity into one message
    reminder_message = f"Reminder: '{task}' is a {priority_message}. {action_message}"

    # Print the reminder message
    print(reminder_message)

# Run the function
daily_reminder()
