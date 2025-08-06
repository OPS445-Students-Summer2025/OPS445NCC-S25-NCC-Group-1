# FUNCTION TO MARK A TASK AS DONE
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
# Main program starts here - # MAIN FUNCTION TO PARSE ARGUMENTS AND CALL FUNCTIONS
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
