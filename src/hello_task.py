import threading
from src.utils import delay

class HelloTask(threading.Thread):
    def __init__(self, message, amount, delay_time=0):
        super().__init__()
        self.message = message
        self.amount = amount
        self.delay_time = delay_time

    def run(self):
        for _ in range(self.amount):
            print(f"Hello, I am Task {self.message}")
            delay(self.delay_time)
