import matplotlib.backends.backend_qtagg as matplotlib_backend_qtagg
import matplotlib.figure as matplotlib_figure
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle

import lib.methods.first_lab.models as methods_first_part_models


class IntersectionAreaPlotter:
    def __init__(
        self,
        a,
        b,
        A,
        B,
        y1_min,
        y1_max,
        c,
        Y,
        G,
        y2_min,
        y2_max,
        x1_min,
        x1_max,
        x2_min,
        x2_max,
    ):
        """
        Initialize the IntersectionAreaPlotter with given parameters.

        Parameters:
            a, b, A, B (float): Coefficients for the first equation y1.
            y1_min, y1_max (float): Minimum and maximum values for y1.
            c, Y, G (float): Coefficients for the second equation y2.
            y2_min, y2_max (float): Minimum and maximum values for y2.
            x1_min, x1_max, x2_min, x2_max (float): Constraints for x1 and x2.
        """
        self.a, self.b, self.A, self.B = a, b, A, B
        self.y1_min, self.y1_max = y1_min, y1_max
        self.c, self.Y, self.G = c, Y, G
        self.y2_min, self.y2_max = y2_min, y2_max
        self.x1_min, self.x1_max, self.x2_min, self.x2_max = (
            x1_min,
            x1_max,
            x2_min,
            x2_max,
        )

        self.generate_grid()

    def generate_grid(self):
        """
        Generate a grid of x1 and x2 values and calculate corresponding y1 and y2 values.
        """
        x1_values = np.linspace(0, 10, 1000)
        x2_values = np.linspace(0, 10, 1000)
        self.x1, self.x2 = np.meshgrid(x1_values, x2_values)

        self.y1 = self.get_y1()
        self.y2 = self.get_y2()

        self.find_intersection()

    def get_y1(self):
        """
        Get y1 values based on the equation y1 = a * x1**A + b * x2**B.
        """
        return self.a * self.x1**self.A + self.b * self.x2**self.B

    def get_y2(self):
        """
        Get y2 values based on the equation y2 = c * x1**Y * x2**G.
        """
        return self.c * self.x1**self.Y * self.x2**self.G

    def find_intersection(self):
        """
        Find the intersection points within the given constraints.
        """
        intersection = np.logical_and(
            (self.y1 >= self.y1_min) & (self.y1 <= self.y1_max),
            (self.y2 >= self.y2_min) & (self.y2 <= self.y2_max),
        )
        self.x1_intersection = self.x1[intersection]
        self.x2_intersection = self.x2[intersection]

    def calculate_percentage_area(self):
        """
        Calculate the percentage area of intersection within the given constraints.
        """
        points = np.array([[x1, y1] for x1, y1 in zip(self.x1_intersection, self.x2_intersection)])
        inside_points = points[
            (points[:, 0] >= self.x1_min)
            & (points[:, 0] <= self.x1_max)
            & (points[:, 1] >= self.x2_min)
            & (points[:, 1] <= self.x2_max)
        ]

        square_area = (self.x1_max - self.x1_min) * (self.x2_max - self.x2_min) * 10 * 1000

        return (inside_points.shape[0] / square_area) * 100


class MplCanvas(matplotlib_backend_qtagg.FigureCanvasQTAgg):
    def __init__(
        self,
        x1,
        x2,
        y1,
        y2,
        y1_min,
        y1_max,
        y2_min,
        y2_max,
        x1_min,
        x1_max,
        x2_min,
        x2_max,
        x1_intersection,
        x2_intersection,
        width=10,
        height=4,
        dpi=100,
    ):
        plt_ = matplotlib_figure.Figure(figsize=(width, height), dpi=dpi)

        self.axes = plt_.add_subplot(111)

        self.axes.contour(
            x1,
            x2,
            y1,
            levels=[y1_min, y1_max],
            colors=["blue", "blue"],
            alpha=0.7,
        )
        self.axes.contour(
            x1,
            x2,
            y2,
            levels=[y2_min, y2_max],
            colors=["red", "red"],
            alpha=0.7,
        )

        rectangle = Rectangle(
            (x1_min, x2_min),
            x1_max - x1_min,
            x2_max - x2_min,
            linewidth=2,
            edgecolor="black",
            facecolor="grey",
            alpha=0.6,
        )
        self.axes.add_patch(rectangle)

        rectangle_outline = Rectangle(
            (x1_min, x2_min),
            x1_max - x1_min,
            x2_max - x2_min,
            linewidth=2,
            edgecolor="black",
            facecolor="none",
            zorder=20,
        )
        self.axes.add_patch(rectangle_outline)

        self.axes.fill_between(
            x1_intersection,
            x2_intersection,
            x2_intersection,
            color="green",
        )

        legend_lines = [
            Line2D([0], [0], color="blue", label="y1(min, max)"),
            Line2D([0], [0], color="red", label="y2(min, max)"),
            Line2D([0], [0], color="green", label="ОБР"),
            Line2D([0], [0], color="black", label="РО"),
        ]

        self.axes.legend(handles=legend_lines)
        self.axes.set_xlabel("x1")
        self.axes.set_ylabel("x2")
        self.axes.grid(which="both", linestyle="--", linewidth=0.5)
        self.axes.set_xticks(np.arange(0, 10.1, 0.1))
        self.axes.set_yticks(np.arange(0, 10.1, 0.1))
        self.axes.tick_params(axis="both", which="major", labelsize=1)

        super(MplCanvas, self).__init__(plt_)


def calculate_method(request: methods_first_part_models.FirstLabModel):
    itersection_area_plotter = IntersectionAreaPlotter(
        a=request.c_x1,
        b=request.c_x2,
        A=request.y1_x1_power,
        B=request.y1_x2_power,
        y1_min=request.y1_min,
        y1_max=request.y1_max,
        c=request.c_y2_constant,
        Y=request.y2_x1_power,
        G=request.y2_x2_power,
        y2_min=request.y2_min,
        y2_max=request.y2_max,
        x1_min=request.x1_min,
        x1_max=request.x1_max,
        x2_min=request.x2_min,
        x2_max=request.x2_max,
    )

    percentage_area = itersection_area_plotter.calculate_percentage_area()
    graph = MplCanvas(
        x1=itersection_area_plotter.x1,
        x2=itersection_area_plotter.x2,
        y1=itersection_area_plotter.y1,
        y2=itersection_area_plotter.y2,
        y1_min=itersection_area_plotter.y1_min,
        y1_max=itersection_area_plotter.y1_max,
        y2_min=itersection_area_plotter.y2_min,
        y2_max=itersection_area_plotter.y2_max,
        x1_min=itersection_area_plotter.x1_min,
        x1_max=itersection_area_plotter.x1_max,
        x2_min=itersection_area_plotter.x2_min,
        x2_max=itersection_area_plotter.x2_max,
        x1_intersection=itersection_area_plotter.x1_intersection,
        x2_intersection=itersection_area_plotter.x2_intersection,
    )
    return f"Площадь пересечения: {percentage_area}%", graph
