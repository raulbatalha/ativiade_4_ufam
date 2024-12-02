import unittest
from src.producer import Producer
from io import StringIO
import sys

class TestProducer(unittest.TestCase):
    def test_producer_output(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        producer = Producer(char="*", repetitions=5, delay_time=0)
        producer.run()

        sys.stdout = sys.__stdout__

        expected_output = "*****"
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
