import pytest
from app import Figure


# Завдання 4: Параметризований тест для всіх дозволених фігур
@pytest.mark.parametrize("fig_type", Figure.FIGURES)
def test_allowed_figures(fig_type):
    fig = Figure(fig_type, 5)
    assert fig.type == fig_type


# Завдання 5: Перевірка фікстури з довжиною 10
def test_figure_length_10_properties(figure_length_10):
    assert figure_length_10.get_figure_length() == 10
    assert figure_length_10.get_figure_type() == "квадрат"


# Завдання 6: Неправильні типи та неправильні значення довжини
@pytest.mark.parametrize("invalid_type", ["коло", "овал", "трапеція"])
def test_invalid_figure_type(invalid_type):
    with pytest.raises(ValueError):
        Figure(invalid_type, 10)


@pytest.mark.parametrize("invalid_length", [0, -1, -10.5])
def test_invalid_figure_length(invalid_length):
    with pytest.raises(ValueError):
        Figure("квадрат", invalid_length)


# Завдання 7: Використання маркера unit
@pytest.mark.unit
def test_square_type():
    fig = Figure("квадрат", 4)
    assert fig.type == "квадрат"


@pytest.mark.unit
def test_triangle_length():
    fig = Figure("трикутник", 3)
    assert fig.get_figure_length() == 3


# Завдання 8: Тести для фікстури зі scope="module"
def test_module_fixture_first_usage(allowed_figures):
    assert "квадрат" in allowed_figures


def test_module_fixture_second_usage(allowed_figures):
    assert len(allowed_figures) == 3