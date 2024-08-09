from lib.find_to_do_tasks import *
import pytest

"""
Given input of string "#TODO"
Returns list containting "#TODO" string
"""
def test_input_todo_returns_list_todo():
    result = find_to_do_tasks("#TODO")
    assert result == ["#TODO"]

"""
Given input of string is 
"This is not a task\n #TODO This is the first task"
Returns list containing first task
"""
def test_input_string_with_todo_and_non_todo_returns_todo_task():
    result = find_to_do_tasks("This is not a task\n#TODO This is the first task")
    assert result == ["#TODO This is the first task"]

"""
Given input of string is "This is not a task\n #TODO This is the first task\n #TODO This is the second task\n This is another note"
Returns list containing two tasks
"""
def test_with_multiple_todos_that_all_todos_are_returned():
    result = find_to_do_tasks("This is not a task\n#TODO This is the first task\n#TODO This is the second task\nThis is another note") 
    assert result == ["#TODO This is the first task", "#TODO This is the second task"]

"""
Given input of string is "This is not a task\n This is the first #TODO task\n #TODO This is the second task\n This is another note"
"""
def test_todo_tasks_still_returned_with_todo_in_middle_of_line():
    result = find_to_do_tasks("This is not a task\nThis is the first #TODO task\n#TODO This is the second task\nThis is another note")
    assert result == ["This is the first #TODO task", "#TODO This is the second task"]

"""
Given input of string is "This is not a task \nThis is also not a task"
Return error message "No tasks to do."
"""
def test_that_no_todos_returns_error_message():
    with pytest.raises(Exception) as e:
        find_to_do_tasks("This is not a task \nThis is also not a task")
    error_message = str(e.value)
    assert error_message == "No tasks to do."
