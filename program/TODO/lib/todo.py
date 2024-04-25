class TODO():
    
    def __init__(self) -> None:
        self.todo_list = []
        
    def list_of_tasks(self, task):
        #Parameters:
        #task: (str)a text, tasks
        self.todo_list.append(task)

    def extract_tasks(self):
        #Returns a list of strings representing tasks
        return self.todo_list

    def complete_tasks(self, completed):
        #Parameters:
        #Remove completed tasks from list
        self.todo_list.remove(completed)