import math
import random

import matplotlib.backends.backend_qtagg as matplotlib_backend_qtagg
import matplotlib.figure as matplotlib_figure
import numpy as np

import lib.methods.second_lab.models as methods_second_part_models

DIGIT_TYPE = int | float


def acceptance_line(a: DIGIT_TYPE, b: DIGIT_TYPE, t: np.ndarray) -> np.ndarray:
    return a + b * t


def rejection_line(c: DIGIT_TYPE, b: DIGIT_TYPE, t: np.ndarray) -> np.ndarray:
    return c + b * t


def trials_f(t: np.ndarray, lambda_: DIGIT_TYPE, b: DIGIT_TYPE) -> np.ndarray:
    mu, sigma = 0, 1

    result = np.zeros_like(t, dtype=float)
    result[0] = 0
    for i in range(len(t)):
        result[i] = result[i - 1]
        if random.random() < lambda_:
            result[i] += abs(np.random.normal(mu, sigma, 1))
    return result + b


class MplCanvas(matplotlib_backend_qtagg.FigureCanvasQTAgg):
    def __init__(
        self, n: int, t_values: np.ndarray, lambda_: float, a: float, b: float, c: float, width=8, height=6, dpi=100
    ):
        plt_ = matplotlib_figure.Figure(figsize=(width, height), dpi=dpi)

        self.axes = plt_.add_subplot(111)
        self.axes.step(n * t_values, trials_f(t_values, lambda_, b), color="black", label="Shit")

        # Линии браковки и приемки
        self.axes.plot(n * t_values, acceptance_line(a, b, t_values), "--", color="green", label="Линия приемки")
        self.axes.plot(n * t_values, rejection_line(c, b, t_values), "--", color="red", label="Линия браковки")

        # Добавление меток и заголовка
        self.axes.set_xlabel("Суммарная наработка для партии из n изделий")
        self.axes.set_ylabel("Количество отказов в партии")
        self.axes.set_title("График испытаний надежности")

        super(MplCanvas, self).__init__(plt_)


def calculate_method(request: methods_second_part_models.SecondLabModel):
    t_max_ = request.t_max / 3600
    t_min_ = request.t_min / 3600
    a = math.log(request.beta / (1 - request.alpha)) / math.log((t_max_ / t_min_))
    b = (1 / t_min_ - 1 / t_max_) / math.log(t_max_ / t_min_)
    c = math.log((1 - request.beta) / request.alpha) / math.log((t_max_ / t_min_))

    t_values = np.linspace(0, request.t_max / 3600, request.n)
    graph = MplCanvas(request.n, t_values, request.lambda_, a, b, c)

    return "Построена область и график", graph
