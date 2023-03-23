def get_uncompleted_tasks(list):
    return get_tasks_by_status(list, False)
    # return uncompleted_tasks



## Get a list of completed tasks
def get_completed_tasks(list):
    return get_tasks_by_status(list, True)
    # return completed_tasks

## Get tasks where time_taken is at least a given time
def get_tasks_taking_at_least(list, time):
    least_time = []
    for task in list:
        if task["time_taken"] >= time:
            least_time.append(task)
    return least_time

## Find a task with a given description
def get_task_with_description(list, description):
    found_task = []
    for task in list:
        if task["description"] == description:
            found_task.append(task)
    return found_task

# Extention (Function): 

## Get a list of tasks by status
def get_tasks_by_status(list, status):
    input_status = []
    for task in list:
        if task["completed"] == status:
            input_status.append(task)
    return input_status

def mark_task_complete(task):
    task["completed"] = True

def create_task(description, time_taken):
    task = {}
    task["description"] = description
    task["completed"] = False
    task["time_taken"] = time_taken

    return task

def add_to_list(list, task):
    list.append(task)

def print_task(task):
    print(f'Description: { task["description"] }')
    print(f'Status: { "Completed" if task["completed"] else "Incomplete"}')
    print(f'Time Taken: {task["time_taken"]} mins')

def print_list(list):
    for task in list:
        print_task(task)