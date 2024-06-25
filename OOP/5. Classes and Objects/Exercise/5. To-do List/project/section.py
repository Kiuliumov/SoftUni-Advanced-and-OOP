class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return 'Task {} is added to the section'.format(new_task.details())
        return 'Task is already in the section {}'.format(self.name)

    def complete_task(self, task_name):
        for task in self.tasks:
            if task_name == task.name:
                task.completed = True
                return 'Completed task {}'.format(task.name)
        return 'Could not find task with the name {}'.format(task_name)

    def clean_section(self):
        cleared_amount = len(self.tasks) - len([task for task in self.tasks if not task.completed])
        self.tasks = [task for task in self.tasks if not task.completed]
        return 'Cleared {} tasks.'.format(cleared_amount)

    def view_section(self):
        string = 'Section {}:\n'.format(self.name)
        for task in self.tasks:
            string += task.details() + '\n'
        return string.strip()
