class Task:
    def __init__(self, title, assignee=None):
        self.title = title
        self.assignee = assignee
        self.status = "todo"  # Default status is "todo"

    def assign_to(self, name):
        self.assignee = name
        self.status = "in progress"  # Update status to "in progress" when assigned
    
    def complete(self):
        self.status = "done"  # Update status to "done" when completed
    
    def __str__(self):
        return f"Task: {self.title}, Assignee: {self.assignee}, Status: {self.status}"
    
my_task = Task("Написать FastAPI сервер")
print(my_task)

my_task.assign_to("Hip")
print(my_task)

my_task.complete()
print(my_task)
