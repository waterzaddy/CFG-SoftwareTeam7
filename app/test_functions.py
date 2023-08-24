import unittest
from functions import todo_length, task_length


class TestTodoListLength(unittest.TestCase):
    # valid case
    def test_todo_valid_length(self):
        todo_list_test = [{"task1": "Sample task", "done": False}, {"task2": "Sample task", "done": False}, {"task3": "Sample task", "done": False}, {"task4": "Sample task", "done": False}, {"task5": "Sample task", "done": False}, {"task6": "Sample task", "done": False}, {"task7": "Sample task8", "done": False}, {"task9": "Sample task", "done": False}]
        self.assertTrue(todo_length(todo_list_test))  # add assertion here

    # boundary case
    def test_todo_max_length(self):
        todo_list_test2 = [{"task1": "Sample task", "done": False}, {"task2": "Sample task", "done": False}, {"task3": "Sample task", "done": False}, {"task4": "Sample task", "done": False}, {"task5": "Sample task", "done": False}, {"task6": "Sample task", "done": False}, {"task7": "Sample task", "done": False}, {"task8": "Sample task", "done": False}, {"task9": "Sample task", "done": False}, {"task10": "Sample task", "done": False}]
        self.assertTrue(todo_length(todo_list_test2))

    # invalid case
    def test_todo_too_long(self):
        todo_list_test2 = [{"task1": "Sample task", "done": False}, {"task2": "Sample task", "done": False}, {"task3": "Sample task", "done": False}, {"task4": "Sample task", "done": False}, {"task5": "Sample task", "done": False}, {"task6": "Sample task", "done": False}, {"task7": "Sample task", "done": False}, {"task8": "Sample task", "done": False}, {"task9": "Sample task", "done": False}, {"task10": "Sample task", "done": False}, {"task11": "Sample task", "done": False}]
        self.assertEqual(False, todo_length(todo_list_test2))

class TestTaskLength(unittest.TestCase):

    def test_task_valid_length(self):
        task_test = "Walk my dog"
        self.assertTrue(task_length(task_test))  # add assertion here

    # boundary case
    def test_task_max_length(self):
        task_test2 = "Lorem ipsum dolor sit amet, consectetur."
        self.assertTrue(task_length(task_test2))

    # invalid case
    def test_task_too_long(self):
        task_test3 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        self.assertEqual(False, task_length(task_test3))


if __name__ == '__main__':
    unittest.main()
