# Recursive Task Listing
# Objective: The objective of this assignment is to introduce students to the concept of recursion by implementing a function to list tasks within a nested hierarchy.

# Problem Statement: You are tasked with implementing a recursive function to list tasks within a hierarchical structure. Each task can have subtasks, forming a nested hierarchy. Your task is to design and implement a recursive function named list_tasks that traverses through the hierarchy and lists tasks in a structured manner.

# Task 1: Design the Task Listing Function

# Design a Python function named list_tasks that takes a single parameter: task_hierarchy. The task_hierarchy parameter represents the nested hierarchy of tasks, where each task is a dictionary with the following keys:

# name: Name or description of the task.
# subtasks: List of subtasks (nested hierarchy), if any.
# The function should traverse through the task hierarchy recursively and list tasks along with their subtasks in a structured format.

def list_tasks(task_hierarchy, indent=0):
    """
    Recursively lists tasks and subtasks from a hierarchical dictionary.
    
    Parameters:
    - task_hierarchy (dict): Dictionary representing the task hierarchy.
    - indent (int): Current level of indentation for formatting (default is 0).
    """
    # Extract task name from the dictionary
    task_name = task_hierarchy['name']
    
    # Print the task name with appropriate indentation
    print(' ' * indent + '- ' + task_name)
    
    # Check if there are subtasks
    if 'subtasks' in task_hierarchy:
        # Recursively list subtasks
        for subtask in task_hierarchy['subtasks']:
            list_tasks(subtask, indent + 2)


# Task 2:  Implement Task Listing Logic

# Implement the task listing logic within the list_tasks function. Use recursion to traverse through the hierarchy and list tasks along with their subtasks. Print each task name and its subtasks (if any) with appropriate indentation to indicate the hierarchy.
def list_tasks(task_hierarchy, indent=0):
    """
    Recursively lists tasks and subtasks from a hierarchical dictionary.
    
    Parameters:
    - task_hierarchy (dict): Dictionary representing the task hierarchy.
    - indent (int): Current level of indentation for formatting (default is 0).
    """
    # Extract task name from the dictionary
    task_name = task_hierarchy['name']
    
    # Print the task name with appropriate indentation
    print(' ' * indent + '- ' + task_name)
    
    # Check if there are subtasks
    if 'subtasks' in task_hierarchy:
        # Recursively list subtasks
        for subtask in task_hierarchy['subtasks']:
            list_tasks(subtask, indent + 2)

# Example task hierarchy
task_hierarchy = {
    'name': 'Main Task 1',
    'subtasks': [
        {
            'name': 'Subtask 1.1',
            'subtasks': []
        },
        {
            'name': 'Subtask 1.2',
            'subtasks': [
               

# Task 3: Test the Task Scheduler Function

# Test your list_tasks function with various task hierarchies, including nested hierarchies with different levels of depth. Verify that tasks are listed correctly in a structured format.

# task_hierarchy_1 = [
#     {
#         "name": "Project",
#         "subtasks": [
#             {"name": "Define project scope"},
#             {"name": "Create project plan"},
#             {"name": "Assign project team",
#             "subtasks": [
#                 {"name": "Identify team members"},
#                 {"name": "Allocate roles and responsibilities"}
#             ]},
#             {"name": "Conduct project kickoff meeting"}
#         ]
#     },
#     {
#         "name": "Research",
#         "subtasks": [
#             {"name": "Gather data"},
#             {"name": "Analyze data",
#             "subtasks": [
#                 {"name": "Data cleaning"},
#                 {"name": "Statistical analysis"}
#             ]},
#             {"name": "Draw conclusions"}
#         ]
#     }
# ]

# task_hierarchy_2 = [
#     {
#         "name": "Homework",
#         "subtasks": [
#             {"name": "Math assignment",
#             "subtasks": [
#                 {"name": "Complete worksheet"},
#                 {"name": "Study for quiz"}
#             ]},
#             {"name": "History essay",
#             "subtasks": [
#                 {"name": "Research topic"},
#                 {"name": "Write essay"}
#             ]}
#         ]
#     },
#     {
#         "name": "Home project",
#         "subtasks": [
#             {"name": "Garden renovation",
#             "subtasks": [
#                 {"name": "Design garden layout"},
#                 {"name": "Purchase plants and materials"}
#             ]},
#             {"name": "DIY furniture",
#             "subtasks": [
#                 {"name": "Select furniture design"},
#                 {"name": "Buy materials"},
#                 {"name": "Assemble furniture"}
#             ]}
#         ]
#     }
# ]

def list_tasks(task_hierarchy, indent=0):
    """
    Recursively lists tasks and subtasks from a hierarchical dictionary.
    
    Parameters:
    - task_hierarchy (dict): Dictionary representing the task hierarchy.
    - indent (int): Current level of indentation for formatting (default is 0).
    """
    # Extract task name from the dictionary
    task_name = task_hierarchy['name']
    
    # Print the task name with appropriate indentation
    print(' ' * indent + '- ' + task_name)
    
    # Check if there are subtasks
    if 'subtasks' in task_hierarchy:
        # Recursively list subtasks
        for subtask in task_hierarchy['subtasks']:
            list_tasks(subtask, indent + 2)

# Test task_hierarchy_1
print("Testing task_hierarchy_1:")
task_hierarchy_1 = [
    {
        "name": "Project",
        "subtasks": [
            {"name": "Define project scope"},
            {"name": "Create project plan"},
            {
                "name": "Assign project team",
                "subtasks": [
                    {"name": "Identify team members"},
                    {"name": "Allocate roles and responsibilities"}
                ]
            },
            {"name": "Conduct project kickoff meeting"}
        ]
    },
    {
        "name": "Research",
        "subtasks": [
            {"name": "Gather data"},
            {
                "name": "Analyze data",
                "subtasks": [
                    {"name": "Data cleaning"},
                    {"name": "Statistical analysis"}
                ]
            },
            {"name": "Draw conclusions"}
        ]
    }
]

list_tasks(task_hierarchy_1)

# Test task_hierarchy_2
print("\nTesting task_hierarchy_2:")
task_hierarchy_2 = [
    {
        "name": "Homework",
        "subtasks": [
            {
                "name": "Math assignment",
                "subtasks": [
                    {"name": "Complete worksheet"},
                    {"name": "Study for quiz"}
                ]
            },
            {
                "name": "History essay",
                "subtasks": [
                    {"name": "Research topic"},
                    {"name": "Write essay"}
                ]
            }
        ]
    },
    {
        "name": "Home project",
        "subtasks": [
            {
                "name": "Garden renovation",
                "subtasks": [
                    {"name": "Design garden layout"},
                    {"name": "Purchase plants and materials"}
                ]
            },
            {
                "name": "DIY furniture",
                "subtasks": [
                    {"name": "Select furniture design"},
                    {"name": "Buy materials"},
                    {"name": "Assemble furniture"}
                ]
            }
        ]
    }
]

list_tasks(task_hierarchy_2)






