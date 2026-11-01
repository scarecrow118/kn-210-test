class Figure:
    FIGURES = ["квадрат", "прямокутник", "трикутник"]

    def __init__(self, figure_type: str, length: float):
        if length <= 0:
            raise ValueError("Довжина має бути більшою за 0")

        if figure_type not in self.FIGURES:
            raise ValueError(f"Невідомий тип фігури: {figure_type}")

        self.type = figure_type
        self.length = length

    def get_figure_type(self) -> str:
        return self.type

    def get_figure_length(self) -> float:
        return self.length