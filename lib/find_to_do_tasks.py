def find_to_do_tasks(notes):
    result = [line for line in notes.split("\n") if "#TODO" in line]
    if result == []:
        raise Exception("No tasks to do.")
    return result