import unittest
from unittest.mock import patch, MagicMock
from app import app


class TestHomeRoute(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_home_route_get_success(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    # testing that the index route doesn't react to "POST"
    def test_home_route_post_failure(self):
        response = self.app.post('/')
        self.assertEqual(response.status_code, 405)


"""TEST OF APP ROUTES FOR HEALTH TO DO LIST"""
# Happiness to do list is a clone of the health to do list so only tests for one of the two is needed


class TestAddHealthTaskRoute(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_add_health_successful(self):
        data = {"todo": "Do yoga"}
        response = self.app.post("/add_health", data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)


class TestEditHealthTaskRoute(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_edit_health_get(self):
        response = self.app.get("/edit_health/0")
        self.assertEqual(response.status_code, 200)

    def test_edit_health_post(self):
        data = {"todo": "New task name"}
        response = self.app.post("/edit_health/0", data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)


class TestCompleteHealthTaskRoute(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()

    def test_complete_health_task_success(self):
        mock_pet_instance = MagicMock()
        mock_pet_instance.health = 50
        mock_pet_instance.min_status = 0
        mock_pet_instance.max_status = 100

        with patch('app.pet', mock_pet_instance):
            mock_todos_health = [{"task": "Sample task", "complete": False}]

            with patch('app.todos_health', mock_todos_health):
                response = self.app.get('/complete_health/0')

                self.assertEqual(response.status_code, 302)

                self.assertTrue(mock_todos_health[0]["complete"])
                # checks that 5 points have been added to health after clicking complete
                self.assertEqual(mock_pet_instance.health, 55)

    def test_complete_health_task_undo(self):
        mock_pet_instance = MagicMock()
        mock_pet_instance.health = 50
        mock_pet_instance.min_status = 0
        mock_pet_instance.max_status = 100

        with patch('app.pet', mock_pet_instance):
            mock_todos_health = [{"task": "Sample task", "complete": True}]

            with patch('app.todos_health', mock_todos_health):
                response = self.app.get('/complete_health/0')

                self.assertEqual(response.status_code, 302)

                self.assertFalse(mock_todos_health[0]["complete"])
                # checks that 5 points have been subtracted from health after clicking complete
                self.assertEqual(mock_pet_instance.health, 45)


class TestDeleteHealthTaskRoute(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()

    def test_delete_completed_health_task(self):
        mock_pet_instance = MagicMock()
        mock_pet_instance.health = 50
        mock_pet_instance.min_status = 0
        mock_pet_instance.max_status = 100

        with patch('app.pet', mock_pet_instance):
            mock_todos_health = [{"task": "Sample task", "complete": True}]

            with patch('app.todos_health', mock_todos_health):
                response = self.app.get('/delete_health/0')

                self.assertEqual(response.status_code, 302)

                # checks that 5 points have been subtracted from health after deleting a completed task
                self.assertEqual(mock_pet_instance.health, 45)

    def test_delete_uncompleted_health_task(self):
        mock_pet_instance = MagicMock()
        mock_pet_instance.health = 50
        mock_pet_instance.min_status = 0
        mock_pet_instance.max_status = 100

        with patch('app.pet', mock_pet_instance):
            mock_todos_health = [{"task": "Sample task", "complete": False}]

            with patch('app.todos_health', mock_todos_health):
                response = self.app.get('/delete_health/0')

                self.assertEqual(response.status_code, 302)

                # checks that health score remains untouched after deleting an uncompleted task
                self.assertEqual(mock_pet_instance.health, 50)


if __name__ == '__main__':
    unittest.main()
