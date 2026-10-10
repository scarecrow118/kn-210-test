import unittest
from task3_app import Figure  # Використовуємо вашу назву файлу task3_app


class TestFigure(unittest.TestCase):

    # ⭐ Завдання 5: Тест довжини фігури
    def test_get_figure_length(self):
        fig = Figure("квадрат", 10)
        self.assertEqual(fig.get_figure_length(), 10)

    # ⭐ Завдання 6: Тести для методу get_angles
    def test_get_angles(self):
        square = Figure("квадрат", 5)
        rectangle = Figure("прямокутник", 8)
        triangle = Figure("трикутник", 3)

        self.assertEqual(square.get_angles(), 4)
        self.assertEqual(rectangle.get_angles(), 4)
        self.assertEqual(triangle.get_angles(), 3)

    # 🔥 Завдання 7: Тести для некоректних даних (винятків)
    def test_zero_length(self):
        with self.assertRaises(ValueError):
            Figure("квадрат", 0)

    def test_negative_length(self):
        with self.assertRaises(ValueError):
            Figure("квадрат", -5)

    def test_unknown_figure_type(self):
        with self.assertRaises(ValueError):
            Figure("коло", 10)


if __name__ == "__main__":
    unittest.main()