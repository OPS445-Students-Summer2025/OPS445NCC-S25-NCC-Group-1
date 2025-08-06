# Winter 2025 Assignment 2
Overview
This Python script is a command-line-based To-Do List Manager that allows users to add, list, and mark tasks as complete. It simulates a basic task management tool for Linux environments, applying skills we've learned in OPS445 such as:

File I/O with JSON
Command-line argument parsing using argparse
Code modularity and teamwork with Git & GitHub


🧑‍🤝‍🧑 Group Members
| Name             | mySeneca Email         | GitHub Username |
| ---------------- | ---------------------- | --------------- |
| Mario Stephenson | `mgstephenson@myseneca.ca` | `MGStephenson`  |
| Member 2 Name    | `ajjeniya@myseneca.ca`     | `Aishajamaljeniya`     |
| Member 3 Name    | `akhatri12`                | `GitHubID3`     |
| Member 4 Name    | `rchoudhary15`             | `rchoudhary15`     |

We collaborated mostly in person and via screen sharing.


⚙️ How to Run
# Add a new task
python3 assignment2.py add "Buy groceries" --due 2025-08-15 --priority high

# List all tasks
python3 assignment2.py list

# Mark a task as done (example: task 1)
python3 assignment2.py done 1


📂 File Structure
| File             | Description                              |
| ---------------- | ---------------------------------------- |
| `assignment2.py` | Main script that runs the task manager   |
| `tasks.json`     | Auto-generated file to store saved tasks |


🧱 Features Implemented
✅ Add a new task with title, due date, and priority
📋 View all tasks
✔️ Mark a task as done
💾 All tasks are stored in tasks.json for persistence


📘 Research / Resources Used
Python argparse documentation - https://docs.python.org/3/library/argparse.html
Working with JSON in Python - https://realpython.com/python-json/
OPS445 Labs 1–8 (especially Lab 2 and Lab 4)


Final Notes
Final version is tagged v1.0 on GitHub
Please use python3 assignment2.py --help for full usage guide
