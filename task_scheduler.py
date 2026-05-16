import heapq

class TaskScheduler:
    def __init__(self):
        self.heap = []
        self.counter = 0

    def add_task(self, task_name, priority):
        heapq.heappush(self.heap, (-priority, self.counter, task_name))
        self.counter += 1
        print(f"Added: '{task_name}' with priority {priority}")

    def execute_task(self):
        if not self.heap:
            print("No tasks to execute.")
            return
        priority, _, task_name = heapq.heappop(self.heap)
        print(f"Executing: '{task_name}' with priority {-priority}")

    def show_tasks(self):
        if not self.heap:
            print("No pending tasks.")
            return
        print("Pending tasks:")
        for priority, _, task_name in sorted(self.heap):
            print(f"  - {task_name} (priority {-priority})")


scheduler = TaskScheduler()

scheduler.add_task("Fix critical bug", 10)
scheduler.add_task("Write documentation", 3)
scheduler.add_task("Code review", 7)
scheduler.add_task("Team meeting", 5)
scheduler.add_task("Deploy to production", 9)

print()
scheduler.show_tasks()

print()
scheduler.execute_task()
scheduler.execute_task()

print()
scheduler.show_tasks()
