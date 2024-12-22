
# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Validate inputs
if priority not in ("high", "medium", "low") or time_bound not in ("yes", "no"):
    print("Invalid input. Please enter a valid priority (high/medium/low) and time-bound (yes/no).")
else:
    # Match case based on priority
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task."
        case "medium":
            reminder = f"'{task}' is a medium priority task."
        case "low":
            reminder = f"'{task}' is a low priority task."

    # Add time sensitivity to the reminder
    if time_bound == "yes":
        reminder += " It requires immediate attention today!"
    else:
        reminder += " Consider completing it when you have free time."

    # Display the reminder
    print("\nReminder:")
    print(reminder)
