# Mario Stephenson
# OPS445 Group Project - My two functions for the To-Do List Manager

# This function adds a new task to the list
def add_task(args):
    tasks = load_tasks()  # load existing tasks - This is from Aisha's Function
# This builds a new task using the data passed from the command line
    # Each task is stored as a dictionary
    task = {
        'title': args.title, # This adds the title (Mandatory)
        'due': args.due, # This adds the due date (Mandatory)
        'priority': args.priority, # This adds the Priority level, low, medium, high (Optional, default is low)
        'done': False  # the task starts as not done
    }

    tasks.append(task)  # add the new task
    save_tasks(tasks)   # save the updated task list
    print("Task has been added.")


# This function shows all the current tasks
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

