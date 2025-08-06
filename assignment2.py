#!/usr/bin/env python3
# Mario Stephenson Aisha Jamal Jeniya Aashish Khatri Raghav Choudhary
# OPS445 Group Project - Simple To-Do List Manager

# Importing necessary built-in Python modules
import argparse    # for handling command-line arguments
import json        # for reading and writing task data to a file
import os          # for checking if a file exists

# ------------------------------
# Global variable for task file
# ------------------------------
FILENAME = 'tasks.json'


# ------------------------------
# Function to load saved tasks
# ------------------------------
def load_tasks():
    # If the file doesn't exist, return an empty list
    if not os.path.exists(FILENAME):
        return []

    # If it exists, open the file and load the data
    with open(FILENAME, 'r') as f:
        return json.load(f)


# ------------------------------
# Function to save tasks
# ------------------------------
def save_tasks(tasks):
    # Write the list of tasks to the file in JSON format
    with open(FILENAME, 'w') as f:
        json.dump(tasks, f, indent=2)


# ------------------------------
# This function adds a new task to the list
# ------------------------------
def add_task(args):
    tasks = load_tasks()  # load existing tasks

    # This builds a new task using the data passed from the command line
    task = {
        'title': args.title,
        'due': args.due,
        'priority': args.priority,
        'done': False  # the task starts as not done
    }

    tasks.append(task)  # add the new task
    save_tasks(tasks)   # save the updated task list
    print("Task has been added.")


# ------------------------------
# This function shows all the current tasks
# ------------------------------
def list_tasks(args):
    tasks = load_tasks()  # get the list of tasks

    # Go through each saved task and print it out in a readable way
    for i, task in enumerate(tasks):
        if task['done']:
            status = "DONE"
        else:
            status = "NOT DONE"

        print("Task", i + 1, ":", task["title"])
        print("   Status:", status)
        print("   Due:", task["due"])
        print("   Priority:", task["priority"])


# ------------------------------
# FUNCTION TO MARK A TASK AS DONE
# ------------------------------
def mark_done(args):
    tasks = load_tasks()                   # Load current tasks from file
    index = int(args.index) - 1            # Convert 1-based to 0-based index

    if 0 <= index < len(tasks):            # Check if index is valid
        tasks[index]['done'] = True        # Mark task as done
        save_tasks(tasks)                  # Save updated tasks to file
        print("Task marked as done.")      # Notify user
    else:
        print("Invalid task number.")      # Error message if invalid index


# ------------------------------
# Main program starts here - MAIN FUNCTION TO PARSE ARGUMENTS AND CALL FUNCTIONS
# ------------------------------
def main():
    parser = argparse.ArgumentParser(description="Simple To-Do List Manager")

    # Sub-commands: add, list, done
    subparsers = parser.add_subparsers()

    # 1. Add task
    parser_add = subparsers.add_parser('add', help='Add a new task')
    parser_add.add_argument('title', help='Title of the task')
    parser_add.add_argument('--due', required=True, help='Due date (e.g., 2025-07-20)')
    parser_add.add_argument('--priority', choices=['low', 'medium', 'high'], default='low')
    parser_add.set_defaults(func=add_task)

    # 2. List tasks
    # This subparser sets up the 'list' command. It connects this command to the list_tasks() function.
    parser_list = subparsers.add_parser('list', help='List all tasks')
    parser_list.set_defaults(func=list_tasks)

    # 3. Mark a task as done
    # This subparser sets up the 'done' command and takes an argument (index) which is the task number.
    # It then passes this info to the mark_done() function.
    parser_done = subparsers.add_parser('done', help='Mark a task as completed')
    parser_done.add_argument('index', help='Task number from the list')
    parser_done.set_defaults(func=mark_done)

    # Parse the arguments from the terminal
    args = parser.parse_args()

    # Run the correct function based on the command
    if hasattr(args, 'func'):
        args.func(args)
    else:
        # If no command is given, display the help message showing how to use the script
        parser.print_help()


# This makes sure the script runs only when you execute it directly
# If this file is imported in another script, it won't run the main() function
if __name__ == '__main__':
    main()
