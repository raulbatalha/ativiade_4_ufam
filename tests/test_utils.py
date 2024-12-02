import unittest
from src.utils import delay
import time

class TestUtils(unittest.TestCase):
    def test_delay(self):
        start_time = time.time()
        delay(0.5)
        end_time = time.time()
        self.assertAlmostEqual(end_time - start_time, 0.5, places=1)

if __name__ == '__main__':
    unittest.main()
