import pydantic


class ThirdLabModel(pydantic.BaseModel):
    lambda_1: float = pydantic.Field(default=0.0001, description="Интенсивность для 1 элемента")
    lambda_2: float = pydantic.Field(default=0.0001, description="Интенсивность для 2 элемента")
    lambda_3: float = pydantic.Field(default=0.0001, description="Интенсивность для 3 элемента")
    lambda_4: float = pydantic.Field(default=0.0001, description="Интенсивность для 4 элемента")
    lambda_5: float = pydantic.Field(default=0.0001, description="Интенсивность для 5 элемента")
    lambda_6: float = pydantic.Field(default=0.0001, description="Интенсивность для 6 элемента")
    lambda_7: float = pydantic.Field(default=0.0001, description="Интенсивность для 7 элемента")
    lambda_8: float = pydantic.Field(default=0.0001, description="Интенсивность для 8 элемента")
    lambda_9: float = pydantic.Field(default=0.0001, description="Интенсивность для 9 элемента")
    lambda_10: float = pydantic.Field(default=0.0001, description="Интенсивность для 10 элемента")

    reserve_1: int = pydantic.Field(default=1, description="Кратность резервирования для 1 элемента")
    reserve_2: int = pydantic.Field(default=1, description="Кратность резервирования для 2 элемента")
    reserve_3: int = pydantic.Field(default=1, description="Кратность резервирования для 3 элемента")
    reserve_4: int = pydantic.Field(default=1, description="Кратность резервирования для 4 элемента")
    reserve_5: int = pydantic.Field(default=1, description="Кратность резервирования для 5 элемента")
    reserve_6: int = pydantic.Field(default=1, description="Кратность резервирования для 6 элемента")
    reserve_7: int = pydantic.Field(default=1, description="Кратность резервирования для 7 элемента")
    reserve_8: int = pydantic.Field(default=1, description="Кратность резервирования для 8 элемента")
    reserve_9: int = pydantic.Field(default=1, description="Кратность резервирования для 9 элемента")
    reserve_10: int = pydantic.Field(default=1, description="Кратность резервирования для 10 элемента")

    t: float = pydantic.Field(default=1000, description="Время")
    accuracy: float = pydantic.Field(default=0.9, description="Необходимая надежность системы")

    variant: int = pydantic.Field(default=..., description="Not expected")

    @pydantic.field_validator(
        "lambda_1",
        "lambda_2",
        "lambda_3",
        "lambda_4",
        "lambda_5",
        "lambda_6",
        "lambda_7",
        "lambda_8",
        "lambda_9",
        "lambda_10",
    )
    @classmethod
    def lambda_limits(cls, value):
        assert 0 < value < 1, ValueError("Интенсивность отказа имеет границы (0, 1)")
        return value

    @pydantic.field_validator(
        "reserve_1",
        "reserve_2",
        "reserve_3",
        "reserve_4",
        "reserve_5",
        "reserve_6",
        "reserve_7",
        "reserve_8",
        "reserve_9",
        "reserve_10",
    )
    @classmethod
    def reserve_limits(cls, value):
        assert value > 0, ValueError("Резервирование должно быть целым числом, больше нуля.")
        return value

    @pydantic.field_validator("accuracy")
    @classmethod
    def accuracy_limits(cls, value):
        assert 0 < value, ValueError("Точность должны быть больше нуля")
        return value

    @pydantic.field_validator("t")
    @classmethod
    def t_limits(cls, value):
        assert value > 0, ValueError("Время должно быть больше нуля")
        return value


class PermanentReserveModel(pydantic.BaseModel):
    lambda_1: float = pydantic.Field(default=0.0001, description="Интенсивность для 1 элемента")
    lambda_2: float = pydantic.Field(default=0.0001, description="Интенсивность для 2 элемента")
    lambda_3: float = pydantic.Field(default=0.0001, description="Интенсивность для 3 элемента")
    lambda_4: float = pydantic.Field(default=0.0001, description="Интенсивность для 4 элемента")
    lambda_5: float = pydantic.Field(default=0.0001, description="Интенсивность для 5 элемента")
    lambda_6: float = pydantic.Field(default=0.0001, description="Интенсивность для 6 элемента")
    lambda_7: float = pydantic.Field(default=0.0001, description="Интенсивность для 7 элемента")
    lambda_8: float = pydantic.Field(default=0.0001, description="Интенсивность для 8 элемента")
    lambda_9: float = pydantic.Field(default=0.0001, description="Интенсивность для 9 элемента")
    lambda_10: float = pydantic.Field(default=0.0001, description="Интенсивность для 10 элемента")

    reserve: int = pydantic.Field(default=1, description="Кратность резервирования для элементов")

    t: float = pydantic.Field(default=1000, description="Время")
    accuracy: float = pydantic.Field(default=0.9, description="Необходимая надежность системы")

    variant: int = pydantic.Field(default=..., description="Not expected")

    @pydantic.field_validator(
        "lambda_1",
        "lambda_2",
        "lambda_3",
        "lambda_4",
        "lambda_5",
        "lambda_6",
        "lambda_7",
        "lambda_8",
        "lambda_9",
        "lambda_10",
    )
    @classmethod
    def lambda_limits(cls, value):
        assert 0 < value < 1, ValueError("Интенсивность отказа имеет границы (0, 1)")
        return value

    @pydantic.field_validator("reserve")
    @classmethod
    def reserve_limits(cls, value):
        assert value > 0, ValueError("Резервирование должно быть целым числом, больше нуля.")
        return value

    @pydantic.field_validator("accuracy")
    @classmethod
    def accuracy_limits(cls, value):
        assert 0 < value, ValueError("Точность должны быть больше нуля")
        return value

    @pydantic.field_validator("t")
    @classmethod
    def t_limits(cls, value):
        assert value > 0, ValueError("Время должно быть больше нуля")
        return value
