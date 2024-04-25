from lib.todo import *

def test_empty_task():
    todo = TODO()
    assert todo.extract_tasks() == []
    
def test_list():
    todo = TODO()
    todo.list_of_tasks("vacuum")
    assert todo.extract_tasks() == ["vacuum"]

def test_complete():
    todo = TODO()
    todo.list_of_tasks("vacuum")
    todo.list_of_tasks("wash up")
    todo.complete_tasks("wash up")
    assert todo.extract_tasks() == ["vacuum"]