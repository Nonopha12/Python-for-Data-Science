import os
import time
from datetime import datetime


script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'user.txt')
task_file_path = os.path.join(script_dir, 'tasks.txt')


#Function to pause and clear screen
def clearScreen():
    time.sleep(0.5)
    os.system('cls')


# Function to read user credentials from file
def read_user_credentials():
    '''
        Reads user credentials from file

            Returns:
                user_credentials
    '''
    user_credentials = {}
    with open(file_path, 'r') as file:
        for line in file:
            try:
                # Split each line into username and password
                username, password = line.strip().split(',')
                # Store username-password pairs in a dictionary
                user_credentials[username] = password
            except ValueError:
                print(f"Issue with line: {line.strip()}. Skipping.")
    return user_credentials


# Function to read tasks from file
def read_tasks():
    '''
        Reads tasks from file

            Returns:
                tasks
    '''
    with open(task_file_path, 'r') as file:
        lines = file.readlines()
        tasks = [line.strip().split(',') for line in lines]
    return tasks


# Function to write user credentials to file
def write_user_credentials(username, password):
    '''
        Writes user credentials to file

        Args:
            username (string): Name of the user that chooses to login 
            password (string): Any characters chosen by user 

            Returns:
                None
    '''
    with open(file_path, 'a') as file:
        # Write username and password in separate lines in file
        file.write(f"\n{username},{password}")


# Function to write task to file
def write_task(username, title, description, due_date):
    '''
        Writes tasks to file

        Args:
            username (string): Name of the user that chooses to login.
            title(string): Heading of the task.
            discription(string): What the task is about.
            due_date(interger): Date in numbers.

            Returns:
                None
    '''
    current_date = datetime.now().strftime('%Y-%m-%d')
    with open(task_file_path, 'a') as file:
        # Write task details in separate lines in file
        file.write(f"\n{username},{title},{description}," +
                   f"{current_date},{due_date},No")


def menu():
    '''
        Gives options of the main menu.

            Returns:
                None
    '''
    # Display main menu options
    print(f"\tPlease select one of the following options:\n")
    print(f"\t\tr - register user\n")
    print(f"\t\ta - add a task\n")
    print(f"\t\tva - view all tasks\n")
    print(f"\t\tvm - view my tasks\n")
    print(f"\t\tgr - generate reports\n")
    print(f"\t\tds - display statistics\n")
    print(f"\t\te - exit")


# Function for user registration when 'r' is selected
def reg_user():
    '''
        Option to register a new user

            Returns:
                None
    '''
    print("User Registration")
    username = input("Enter a new username: ")
    user_credentials = read_user_credentials()
    while username in user_credentials:
        clearScreen()
        print("Username already exists! Please choose a new user name")
        username = input("Enter a new username: ")

    password = input("Enter a new password: ")
    confirm_password = input("Confirm your password: ")

    if password == confirm_password:
        # Write new user credentials to file
        write_user_credentials(username, password)
        print("User registered successfully.")
    else:
        print("Passwords do not match. Registration failed.")


#Function to add new task when 'a' is selected.
def add_task():
    '''
       Option to add a new task

            Returns:
                None
    '''
    users = read_user_credentials()

    task_username = input("Enter the username of the " +
                          "person the task is assigned to: ")
    if not task_username in users.keys():
        print("User not registered")
        return
    
    task_title = input("Enter the title of the task: ")
    task_description = input("Enter a description of the task: ")
    task_due_date = input("Enter the due date of the task (YYYY-MM-DD): ")
    write_task(task_username, task_title,
               task_description, task_due_date)
    print("Task added successfully.")


# Function to display all tasks when 'va' is selected
def view_all(tasks):
    '''
        Writes user credentials to file

        Args:
            tasks(list): tasks of a specific user
            
            Returns:
                None
    '''
    for task in tasks:
        # Display task details for each task
        print(f"Assigned to: {task[0]}")
        print(f"Title: {task[1]}")
        print(f"Description: {task[2]}")
        print(f"Assigned Date: {task[3]}")
        print(f"Due Date: {task[4]}")
        print(f"Completed: {task[5]}\n")


# Function to display my tasks when 'vm' is selected
def view_mine(username, tasks):
    '''
        This function is used to show all tasks assigned to a specified user

        Args:
            username (string): Name the user that is wants to display tasks.
            tasks (list): List of tasks

            Returns:
                None
    '''
    # Initialize counter
    task_counter = 0

    # Append tasks into array for better and easier manipulation
    user_tasks = []

    # Create counter
    for task in tasks:
        # Display task details if assigned to current user
        if task[0] == username:
            task_counter += 1
            user_tasks.append(task)

            print(f"\t{task_counter}. {task[1]}")

    if task_counter == 0:
        clearScreen()
        print("No tasks found for the active user")
        return

    while True:

        task_selection = int(input("\nEnter the number of task to view \
                                   details or -1 to return to main menu: "))
        if task_selection == -1:
            return
        elif 1 <= task_selection <= task_counter:
            clearScreen()
            selected_task = user_tasks[task_selection - 1]
            print(f"\nTask {task_selection} Details")
            print(f"\tTitle: {selected_task[1]}")
            print(f"\tDescription: {selected_task[2]}")
            print(f"\tAssigned Date: {selected_task[3]}")
            print(f"\tDue Date: {selected_task[4]}")
            print(f"\tCompleted: {selected_task[5]}\n")

            # Choice for user to mark the task as complete or edit the task
            action = input(
                "Do you want to mark this task as complete (enter 'c') or \
                    edit this task (enter 'e')? ").lower()
            if action == 'c':
                selected_task[5] = 'Yes'
                print("Task marked as complete.")
            elif action == 'e':
                if selected_task[5] == 'Yes':
                    print("This task is already marked as complete and cannot\
                           be edited.")
                    time.sleep(1.5)
                    print("returning to main menu...")
                    clearScreen()
                else:
                    edit_option = input(
                        "Do you want to edit the username of the person to \
                            whom the task is assigned (enter 'u') or the \
                                due date (enter 'd')? ").lower()
                    if edit_option == 'u':
                        new_username = input("Enter the new username: ")
                        selected_task[0] = new_username
                    elif edit_option == 'd':
                        new_due_date = input("Enter the new due date \
                                             (YYYY-MM-DD): ")
                        try:
                            datetime.strptime(new_due_date, "%Y-%m-%d")
                            selected_task[4] = new_due_date
                        except ValueError:
                            print("Invalid date format. Please enter the date\
                                   in YYYY-MM-DD format.")
                            continue
                    else:
                        print("Invalid edit option. Please enter \
                              either 'u' or 'd'.")
                        continue

                    print("Task edited successfully.")
            else:
                print("Invalid action. Please enter either 'c' or 'e'.")

            # Rewrite the updated tasks to tasks.txt
            with open(task_file_path, "w") as file:
                for task in tasks:
                    file.write(",".join(task) + "\n")
            return

        else:
            print("Invalid selection. Please enter task")


# Function to generate reports
def generate_reports():
    '''
        This function is used to generate reports 

            Returns:
                None
    '''
    with open("task_overview.txt", "w") as file:
        tasks = read_tasks()
        task_count = len(tasks)
        tasks_completed = sum([1 if task[5] == "Yes" else 0 for task in tasks])
        tasks_incompleted_n = task_count - tasks_completed
        tasks_incompleted = []
        tasks_overdued = []

        for task in tasks:
            if task[5] == "Yes":
                continue

            tasks_incompleted.append(task)

            due_date_string = task[4]
            due_date = datetime.strptime(due_date_string, "%Y-%m-%d")

            if due_date < datetime.now():
                tasks_overdued.append(task)

        tasks_overdued_n = len(tasks_overdued)

        percentage_incompleted = tasks_incompleted_n / task_count * 100
        percentage_overdued = tasks_overdued_n / tasks_incompleted_n * 100

        file.write(
            f"No. of Tasks: {task_count}\n"
            f"Completed: {tasks_completed}\n"
            f"Incomplte: {tasks_incompleted_n}\n"
            f"Tasks overdue: {len(tasks_overdued)}\n"
            f"Incomplete%: {percentage_incompleted}\n"
            f"Complete%: {percentage_overdued}"
        )

    users = read_user_credentials()
    user_count = len(users)
    with open("user_overview.txt", "w") as file:  # To write to the txt file
        file.write(f"{user_count}")

    with open("user_overview.txt", "a") as file:  # To append to the txt file

        for user in users.keys():
            tasks = read_tasks()
            user_tasks = []

            for task in tasks:
                username = task[0]

                if username == user:
                    user_tasks.append(task)

            user_tasks_percentage = 0
            tasks_completed_percentage = 0

            task_count = len(user_tasks)  # Amount of tasks assigned to user
            try:
                user_tasks_percentage = task_count / len(tasks) * 100

                tasks_completed = sum([1 if task[5] == "Yes" else 0 for task \
                                       in user_tasks])
                tasks_completed_percentage = tasks_completed / task_count * 100
            except ZeroDivisionError:
                print("Can not perform the percentage of tasks completed.")

            tasks_todo_percentage = 100 - tasks_completed_percentage

            tasks_incompleted = []
            tasks_overdued = []

            for task in user_tasks:
                if task[5] == "Yes":
                    continue

                tasks_incompleted.append(task)

                due_date_string = task[4]
                due_date = datetime.strptime(due_date_string, "%Y-%m-%d")

                if due_date < datetime.now():
                    tasks_overdued.append(task)

            tasks_overdued_n = len(tasks_overdued)

            try:
                percentage_overdued = tasks_overdued_n / len(tasks_incompleted)
            except ZeroDivisionError:
                percentage_overdued = 0

            file.write(
                f"\nUserername: {user}\n"
                f"Tasks: {task_count}\n"
                f"Tasks%: {user_tasks_percentage}\n"
                f"Completed%: {tasks_completed_percentage}\n"
                f"Tasks_To_Do%: {tasks_todo_percentage}\n"
                f"Overdue%: {percentage_overdued}"
                )


# Function to display statistics
def display_statistics():
    '''
        Displays the statistics of the tasks

            Returns:
                None
    '''
    with open("user_overview.txt", "r") as f:
        data = "".join(f.readlines())
        print(data)

    with open("task_overview.txt", "r") as f:
        data = "".join(f.readlines())
        print(data)

if __name__ == "__main__":
    # Main program loop
    while True:
        # Read user credentials and tasks from files
        user_credentials = read_user_credentials()
        tasks = read_tasks()
        # Prompt user to enter username and password
        username = input("\tEnter your username: ")
        password = input("\tEnter your password: ")
        is_admin = username == "admin"
        # Validate user login
        if username in user_credentials \
            and user_credentials[username] == password:
            print("\tLogin successful!")
            clearScreen()
            while True:

                # Display main menu options
                menu()
                choice = input(": ").lower()
                if choice == 'r':
                    if username == 'admin':
                        clearScreen()
                        reg_user()
                    else:
                        print("Only the admin user can register new users.")
                elif choice == 'a':
                    # Prompt user to enter task details and add task
                    clearScreen()
                    add_task()

                elif choice == 'va':
                    # Display all tasks
                    clearScreen()
                    print("All Tasks:")
                    view_all(tasks)

                elif choice == 'vm':
                    # Display my tasks
                    clearScreen()
                    print("Your Tasks:")
                    view_mine(username, tasks)
                    time.sleep(0.5)
                    clearScreen()

                elif choice == "gr":
                    if is_admin:
                        generate_reports()
                    else:
                        print("You are not allowed to generate reports")

                elif choice == 'ds':
                    # Display statistics
                    if is_admin:
                        generate_reports()
                    else:
                        print("You are not allowed to generate reports")

                        clearScreen()
                        display_statistics()
                elif choice == 'e':
                    print('Menu exited. Goodbye!!!')
                    exit()
                else:
                    clearScreen()
                    print("Invalid input. Please try again.")
        else:
            print("Invalid username or password. Please try again")
