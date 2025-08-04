#!/usr/bin/env python3
# Author: rchoudhary15
# Script for listing tasks and marking them as done using argparse (based on OPS445 Lab 1–8)

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
# This line uses argparse to read the user's command and options entered in the terminal
args = parser.parse_args()

# Run the correct function based on the command
# If the user typed a valid command (like list, done), the corresponding function is called
if hasattr(args, 'func'):
    args.func(args)
else:
    # If no command is given, display the help message showing how to use the script
    parser.print_help()

# This makes sure the script runs only when you execute it directly
# If this file is imported in another script, it won't run the main() function
if __name__ == '__main__':
    main()

