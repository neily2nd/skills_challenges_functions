# File: test_todo_list.py
import pytest
from lib.todo_list import *


def test_add():
    todo_list = TodoList()
    todo_list.add(Todo("Task 1"))
    assert len(todo_list.todos) == 1

def test_incomplete():
    todo_list = TodoList()
    todo1 = Todo("Task 1")
    todo2 = Todo("Task 2")
    todo2.mark_complete()
    todo_list.add(todo1)
    todo_list.add(todo2)
    assert len(todo_list.incomplete()) == 1

def test_complete():
    todo_list = TodoList()
    todo1 = Todo("Task 1")
    todo2 = Todo("Task 2")
    todo2.mark_complete()
    todo_list.add(todo1)
    todo_list.add(todo2)
    assert len(todo_list.complete()) == 1

def test_give_up():
    todo_list = TodoList()
    todo1 = Todo("Task 1")
    todo2 = Todo("Task 2")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.give_up()
    assert all(todo.complete for todo in todo_list.todos)
