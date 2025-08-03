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
