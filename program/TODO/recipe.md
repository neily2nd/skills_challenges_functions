# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

class TODO():
    def list_of_tasks(self, task):
        #Parameters:
        #task: (str)a text, tasks
        pass

    def extract_tasks(self):
        #Returns a list of strings representing tasks
        pass

    def complete_tasks(self, completed):
        #Parameters:
        #Remove completed tasks from list
        pass

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

```python

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








```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
