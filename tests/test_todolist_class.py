

from lib.todo_class import *
from lib.todolist_class import *
import pytest


""" 

UNIT TESTS for TODO_LIST class

Nothing here from TODO_CLASS - may make it difficult to test thouroughly

"""


# first test just checks object and class exists


def test_todo_list_exists():

    test_todolist = TodoList()

    assert test_todolist != None


# second test checks if a list with tasks is created


def test_todo_list_exists_with_dict():

    test_todolist = TodoList()

    result = test_todolist.tasklist 

    assert result == []


#second test just checks functionality of all methods if no tasks are added
# should return an error

def test_todo_list_no_tasks():

    test_todolist = TodoList()    

    with pytest.raises(Exception) as e:
        test_todolist.incomplete()
    error_message = str(e.value)
    assert error_message == "No tasks in list!"

    with pytest.raises(Exception) as e:
        test_todolist.complete()
    error_message = str(e.value)
    assert error_message == "No tasks in list!"

    with pytest.raises(Exception) as e:
        test_todolist.give_up()
    error_message = str(e.value)
    assert error_message == "No tasks in list!"



