import threading
import random
from src.utils import delay
import config.config as cfg

class BikeComputer(threading.Thread):
    def __init__(self):
        super().__init__()
        self.state = "Viagem"
        self.total_distance = 0
        self.trip_distance = 0
        self.trip_time = 0

    def run(self):
        while True:
            if self.state == "Viagem":
                self.display_trip_distance()
                delay(cfg.DISPLAY_INTERVAL_VIAGEM)
            elif self.state == "Velocidade":
                self.display_speed()
                delay(cfg.DISPLAY_INTERVAL_VELOCIDADE)
            elif self.state == "Total":
                self.display_total_distance()
                delay(cfg.DISPLAY_INTERVAL_TOTAL)
            elif self.state == "Time":
                self.display_time()
                delay(cfg.DISPLAY_INTERVAL_TIME)

    def display_trip_distance(self):
        print(f"Trip Distance: {self.trip_distance:.2f} km")

    def display_speed(self):
        speed = random.uniform(20, 40)
        print(f"Speed: {speed:.2f} km/h")

    def display_total_distance(self):
        print(f"Total Distance: {self.total_distance:.2f} km")

    def display_time(self):
        print(f"Time: {self.trip_time} s")
