import typing

import lib.methods.first_lab as methods_first_lab
import lib.methods.second_lab as methods_second_lab
import lib.methods.third_lab as methods_third_lab

LAB_1_METHODS: dict[str, typing.Any] = {
    "Метод граничных испытаний на надежность": (methods_first_lab.FirstLabModel, methods_first_lab.laba1_calculate),
}

LAB_2_METHODS: dict[str, typing.Any] = {
    "Метод последовательного анализа при испытании на надежность": (
        methods_second_lab.SecondLabModel,
        methods_second_lab.laba2_calculate,
    ),
}


LAB_3_METHODS: dict[str, typing.Any] = {
    "Постоянное резервирование": (
        methods_third_lab.PermanentReserveModel,
        methods_third_lab.permanent_reserve_calculate,
    ),
    "Резервирование замещением": (methods_third_lab.ThirdLabModel, methods_third_lab.rolling_reserve_calculate),
    "Скользящее резервирование": (methods_third_lab.ThirdLabModel, methods_third_lab.replacement_reserve_calculate),
}


FIELD_DEFAULT_TYPE = str | int | float | None
