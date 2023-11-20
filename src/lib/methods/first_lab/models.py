import pydantic


class FirstLabModel(pydantic.BaseModel):
    x1_min: float = pydantic.Field(default=1, description="Нижняя граница x1")
    x1_max: float = pydantic.Field(default=2, description="Верхняя граница x1")
    x2_min: float = pydantic.Field(default=1, description="Нижняя граница x2")
    x2_max: float = pydantic.Field(default=2, description="Верхняя граница x2")
    y1_min: float = pydantic.Field(default=5, description="Нижняя граница y1")
    y1_max: float = pydantic.Field(default=15, description="Верхняя граница y1")
    y2_min: float = pydantic.Field(default=2, description="Нижняя граница y2")
    y2_max: float = pydantic.Field(default=10, description="Верхняя граница y2")
    c_y2_constant: float = pydantic.Field(default=0.5, description='Константа "c" для y2')
    y1_x1_power: float = pydantic.Field(default=2, description="Степень x1 для y1")
    y1_x2_power: float = pydantic.Field(default=3, description="Степень x2 для y1")
    y2_x1_power: float = pydantic.Field(default=1, description="Степень x1 для y2")
    y2_x2_power: float = pydantic.Field(default=2, description="Степень x2 для y2")
    c_x1: float = pydantic.Field(default=1, description="Значение C для x1")
    c_x2: float = pydantic.Field(default=2, description="Значение C для x2")

    # c_max: float = pydantic.Field(default=0, description="Максимальное значение C")
    # probability: float = pydantic.Field(default=0, description="Вероятность")
    # accuracy: float = pydantic.Field(default=0, description="Точность")

    @pydantic.field_validator(
        "x1_min",
        "x1_max",
        "x2_min",
        "x2_max",
        "y1_min",
        "y1_max",
        "y2_min",
        "y2_max",
        "c_y2_constant",
        "y1_x1_power",
        "y1_x2_power",
        "y2_x1_power",
        "y2_x2_power",
        "c_x1",
        "c_x2",
    )
    @classmethod
    def check_limits(cls, value: float) -> float:
        assert 0 < value, ValueError("Значение не может быть меньше 0")
        return value

    # @pydantic.field_validator("probability")
    # @classmethod
    # def probability_limits(cls, value: float) -> float:
    #     assert 0 < value < 1, ValueError("Вероятность должна быть в пределах (0, 1)")
    #     return value
    #
    # @pydantic.field_validator("accuracy")
    # @classmethod
    # def accuracy_limits(cls, value: float) -> float:
    #     assert 0 < value < 1, ValueError("Точность должна быть в пределах (0, 1)")
    #     return value
