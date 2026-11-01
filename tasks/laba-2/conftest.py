import pytest
from app import Figure


# Фікстура зі scope="module" (Завдання 8)
@pytest.fixture(scope="module")
def allowed_figures():
    return Figure.FIGURES


# Фікстура, що повертає фігуру з довжиною 10 (Завдання 5)
@pytest.fixture
def figure_length_10():
    return Figure("квадрат", 10)