# ------------------------------
# Function to save tasks
# ------------------------------
def save_tasks(tasks):
    # Write the list of tasks to the file in JSON format
    with open(FILENAME, 'w') as f:
        json.dump(tasks, f, indent=2)
