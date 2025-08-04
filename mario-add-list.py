# Mario Stephenson
# OPS445 Group Project - My two functions for the To-Do List Manager

# This function adds a new task to the list
def add_task(args):
    tasks = load_tasks()  # load existing tasks

    # Each task is stored as a dictionary
    task = {
        'title': args.title,
        'due': args.due,
        'priority': args.priority,
        'done': False  # the task starts as not done
    }

    tasks.append(task)  # add the new task
    save_tasks(tasks)   # save the updated task list
    print("Task has been added.")


# This function shows all the current tasks
def list_tasks(args):
    tasks = load_tasks()  # get the list of tasks

    # Loop through each task and display it
    for i, task in enumerate(tasks):
        if task['done']:
            status = "DONE"
        else:
            status = "NOT DONE"

        print(f"{i + 1}. [{status}] {task['title']} - Due: {task['due']} - Priority: {task['priority']}")


# Only run this test if this file is executed directly
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("title")
    parser.add_argument("--due", required=True)
    parser.add_argument("--priority", default="low")
    args = parser.parse_args()
    
    add_task(args)
    list_tasks(args)
