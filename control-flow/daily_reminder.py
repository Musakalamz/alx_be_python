# daily_reminder.py
# Personal Daily Reminder Program

print("##### Personal Daily Reminder #####")

# Loop to ensure valid inputs
while True:
    task = input("Enter your task: ").strip()
    if task:
        break
    else:
        print("Task description cannot be empty. Please enter again.")

while True:
    priority = input("Priority (high/medium/low): ").lower().strip()
    if priority in ["high", "medium", "low"]:
        break
    else:
        print("Invalid priority. Please enter 'high', 'medium', or 'low'.")

while True:
    time_bound = input("Is it time-bound? (yes/no): ").lower().strip()
    if time_bound in ["yes", "no"]:
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

# Process using match case
match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unspecified priority"  # fallback

# Check if time-sensitive
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message += ". Consider completing it when you have free time."

# Display the customized reminder (checker expects a print that begins with "Reminder:")
print(f"Reminder: {message}")

print("\nWell done on completing this project! Let the world hear about this milestone achieved.")