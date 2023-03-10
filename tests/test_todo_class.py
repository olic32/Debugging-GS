from lib.todo_class import *
from lib.todolist_class import *
import pytest



""" 

UNIT TESTS for TODO_CLASS

No integrated testing in this file

TODO_CLASS is a simple containter for a task and boolean for whether it has been
completed or not

used within the greater functionality of the TODO_LIST class

"""



# First test, simply checks the existence of TODO_class obj, and whether it contains
# the necessary locals

def test_todo_has_string_and_boolean():
    test_todo = Todo("Walk the dog")

    result_str = test_todo.task
    result_bool = test_todo.complete

    assert type(result_str) == str
    assert type(result_bool) == bool



#second test checks that if a mark complete is performed, the bool changes

def test_mark_complete_chanes_bool():
    test_todo = Todo("Walk the dog")

    assert test_todo.task == "Walk the dog"
    assert test_todo.complete == False

    test_todo.mark_complete()

    assert test_todo.task == "Walk the dog"
    assert test_todo.complete == True


#test checks if running mark complete twice has any effect

def test_mark_complete_chanes_bool():
    test_todo = Todo("Walk the dog")

    assert test_todo.task == "Walk the dog"
    assert test_todo.complete == False

    test_todo.mark_complete()

    test_todo.mark_complete()

    assert test_todo.task == "Walk the dog"
    assert test_todo.complete == True