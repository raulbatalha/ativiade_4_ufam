import unittest
from src.bike_computer import BikeComputer

class TestBikeComputer(unittest.TestCase):
    def setUp(self):
        self.bike_computer = BikeComputer()

    def test_initial_state(self):
        self.assertEqual(self.bike_computer.state, "Viagem")
        self.assertEqual(self.bike_computer.total_distance, 0)
        self.assertEqual(self.bike_computer.trip_distance, 0)
        self.assertEqual(self.bike_computer.trip_time, 0)

    def test_trip_distance_update(self):
        self.bike_computer.trip_distance += 1
        self.bike_computer.total_distance += 1
        self.assertEqual(self.bike_computer.trip_distance, 1)
        self.assertEqual(self.bike_computer.total_distance, 1)

if __name__ == '__main__':
    unittest.main()
