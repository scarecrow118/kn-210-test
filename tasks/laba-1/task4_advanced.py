import unittest
from unittest.mock import patch
from task3_app import Figure  # Імпортуємо з вашого файлу task3_app


# Допоміжна функція з input() для Завдання 5
def get_user_figure_length():
    user_input = input("Введіть довжину фігури: ")
    return float(user_input)


class TestAdvancedFeatures(unittest.TestCase):

    # ⭐ Завдання 4: Тест із subTest для всіх типів Figure
    def test_all_figure_types_with_subtest(self):
        test_cases = [
            ("квадрат", 5, 4),
            ("прямокутник", 10, 4),
            ("трикутник", 3, 3),
        ]
        for f_type, length, expected_angles in test_cases:
            with self.subTest(figure_type=f_type, length=length):
                fig = Figure(f_type, length)
                self.assertEqual(fig.get_figure_type(), f_type)
                self.assertEqual(fig.get_figure_length(), length)
                self.assertEqual(fig.get_angles(), expected_angles)

    # ⭐ Завдання 5: Тестування функції з input() за допомогою patch
    @patch("builtins.input", return_value="15.5")
    def test_get_user_figure_length(self, mock_input):
        result = get_user_figure_length()
        self.assertEqual(result, 15.5)
        mock_input.assert_called_once_with("Введіть довжину фігури: ")


if __name__ == "__main__":
    unittest.main()