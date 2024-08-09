## 1. Describe the Problem

As a user
So that I can find my tasks among all my notes
I want to check if a line from my notes includes the string `#TODO`.

## 2. Design the Function Signature

find_to_do():
parameters:  notes (string)
return value: list of strings starting with to do
side effects: none

```python
# EXAMPLE

def find_to_do_tasks(notes):
    """finds TODO tasks from notes so user knows what tasks need to be done

    Parameters: (list all parameters and their types)
        notes: a string containing words (e.g. "hello WORLD")
    
    Returns:
        a list of strings that begin with the characters '#TODO' and end with '\n'

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
function input is a string 
Returns True if input is a string 
"""
find_to_do_tasks("string") => True


"""
Given input of string "#TODO"
Returns list containting "#TODO" string
"""
find_to_do_tasks("#TODO") => ["#TODO"]

"""
Given input of string is "This is not a task\n #TODO This is the first task"
Returns list containing first task
"""
find_to_do_tasks("This is not a task\n #TODO This is the first task") => ["#TODO This is the first task"]

"""
Given input of string is "This is not a task\n #TODO This is the first task\n #TODO This is the second task\n This is another note"
Returns list containing two tasks
"""
find_to_do_tasks("This is not a task\n #TODO This is the first task\n #TODO This is the second task\n This is another note") => ["#TODO This is the first task", "#TODO This is the second task"]

"""
Given input of string is "This is not a task\n This is the first #TODO task\n #TODO This is the second task\n This is another note"
"""


find_to_do_tasks("This is not a task\n This is the first #TODO task\n #TODO This is the second task\n This is another note") => ["This is the first #TODO task", "#TODO This is the second task"]

"""
Given input of string is "This is not a task \n This is also not a task"
Return error message "No tasks to do."
"""
find_to_do_tasks("This is not a task \n This is also not a task") => "No tasks to do."
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
