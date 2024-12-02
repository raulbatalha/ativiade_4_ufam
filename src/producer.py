import threading
from src.utils import delay

class Producer(threading.Thread):
    def __init__(self, char, repetitions=10, delay_time=0):
        super().__init__()
        self.char = char
        self.repetitions = repetitions
        self.delay_time = delay_time
        self.control = True

    def run(self):
        for _ in range(self.repetitions):
            if not self.control:
                break
            print(self.char, end="")
            delay(self.delay_time)

    def terminate(self):
        self.control = False
