import typing

import lib.methods.second_lab as methods_second_lab
import lib.methods.third_lab as methods_third_lab

LAB_2_METHODS: dict[str, typing.Any] = {
    "загрузка": (methods_second_lab.SecondLabModel, methods_second_lab.laba2_calculate),
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
