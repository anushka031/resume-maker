import time

response = input("Welcome to Resume Maker\nDo you want to make a resume (yes/no)? ")
if response.lower() == 'yes':
    print("Starting up with a few questions...")
  

# Set the countdown duration
    sleep_duration = 5  # Replace this with the desired number of seconds

# Countdown loop
    for i in range(sleep_duration, 0, -1):
     print(i)  # Print the countdown number
    time.sleep(1)  # Pause for 1 second between each number
    print("Time's up!")

    
    # Collect user details
    name = input("Enter your full name: ")
    
    while True:
        contact_number = input("Enter your 10-digit contact number: ")

        if contact_number.isdigit() and len(contact_number) == 10:
            print("Perfect!!")
            break  # Exit the loop when the contact number is valid
        else:
            print("Please enter a valid 10-digit contact number.")
    
    skills = input("Enter your skills: ")
    grad = input("Are you graduated (yes/no)? ").lower()

    if grad == 'yes':
        print("Resume coming right up...")
        resume = {
            "Name": name,
            "Contact Number": contact_number,
            "Skills": skills
        }
        print("\nYour Resume:\n", resume)
    else:
        print("Graduation is necessary for creating a resume.")
else:
    print("Ending the process.")

