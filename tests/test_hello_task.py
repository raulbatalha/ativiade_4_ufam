import unittest
from src.hello_task import HelloTask
from io import StringIO
import sys

class TestHelloTask(unittest.TestCase):
    def test_hello_task_output(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        task = HelloTask("Test", amount=3)
        task.run()

        sys.stdout = sys.__stdout__

        expected_output = "Hello, I am Task Test\n" * 3
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
