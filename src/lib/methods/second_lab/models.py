import typing

import pydantic


class SecondLabModel(pydantic.BaseModel):
    t_min: float = pydantic.Field(default=3000, description="Нижняя граница времени (TH)")
    t_max: float = pydantic.Field(default=5000, description="Верхняя граница времени (TB)")
    n: int = pydantic.Field(default=20, description="Количество отказов (n)")
    max_time: int = pydantic.Field(default=10000, description="Максимальное время")
    lambda_: float = pydantic.Field(default=0.1, description="Интенсивность (lambda)")
    alpha: float = pydantic.Field(default=0.1, description="Риск поставщика (alpha)")
    beta: float = pydantic.Field(default=0.1, description="Риск приемщика (потребителя) (beta)")

    @pydantic.field_validator("lambda_")
    @classmethod
    def lambda_limits(cls, value: float) -> float:
        assert 0 < value < 1, ValueError("Интенсивность отказа имеет границы (0, 1)")
        return value

    @pydantic.field_validator("alpha")
    @classmethod
    def alpha_limits(cls, value: float) -> float:
        assert 0 < value < 1, ValueError("Риск поставщика имеет границы (0, 1)")
        return value

    @pydantic.field_validator("beta")
    @classmethod
    def beta_limits(cls, value: float) -> float:
        assert 0 < value < 1, ValueError("Риск приемщика имеет границы (0, 1)")
        return value

    @pydantic.field_validator("n")
    @classmethod
    def n_limits(cls, value: int) -> int:
        assert value > 0, ValueError("Количество отказов должно быть больше нуля")
        return value

    @pydantic.field_validator("t_min")
    @classmethod
    def time_min_limits(cls, value: float) -> float:
        assert value > 0, ValueError("Минимальное время должно быть больше нуля")
        return value

    @pydantic.field_validator("t_max")
    @classmethod
    def time_max_limits(cls, value: float) -> float:
        assert value > 0, ValueError("Максимальное время должно быть больше нуля")
        return value

    @pydantic.model_validator(mode="after")
    def check_time(self) -> typing.Self:
        assert self.t_min < self.t_max, ValueError("Минимальное время должно быть меньше максимального")
        return self
