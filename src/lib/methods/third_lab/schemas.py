import math
import typing


def get_forward(probabilities: typing.Iterable[int | float]) -> int | float:
    """get forward connection probability"""
    return math.prod(probabilities)


def get_parallel(probability_1: int | float, probability_2: int | float) -> int | float:
    """get parallel connection probability"""
    return 1 - (1 - probability_1) * (1 - probability_2)


def get_probability_schema_1(probabilities: list[float | int]) -> int | float:
    pp1 = get_parallel(get_parallel(probabilities[0], probabilities[1]), probabilities[2])
    pp2 = get_parallel(
        get_parallel(
            get_parallel(get_parallel(probabilities[3], probabilities[4]), probabilities[5]), probabilities[6]
        ),
        probabilities[7],
    )

    return get_forward([pp1, pp2, probabilities[8], probabilities[9]])


def get_probability_schema_2(probabilities: list[float | int]) -> int | float:
    pp1 = get_parallel(probabilities[1], probabilities[2])
    pp2 = get_parallel(probabilities[4], probabilities[5])
    pp3 = get_parallel(probabilities[6], get_forward([probabilities[7], probabilities[8]]))

    return get_forward([probabilities[1], pp1, probabilities[3], pp2, pp3, probabilities[9]])


def get_probability_schema_3(probabilities: list[float | int]) -> int | float:
    pp1 = get_parallel(get_parallel(probabilities[0], probabilities[1]), probabilities[2])
    pp2 = get_parallel(get_parallel(probabilities[3], probabilities[4]), probabilities[5])
    pp3 = get_parallel(probabilities[6], probabilities[7])

    return get_forward([pp1, pp2, pp3, probabilities[8], probabilities[9]])


def get_probability_schema_4(probabilities: list[float | int]) -> int | float:
    pp1 = get_parallel(probabilities[0], probabilities[1])
    pp2 = get_parallel(
        get_forward([probabilities[3], probabilities[4]]),
        get_forward([get_parallel(probabilities[5], probabilities[8]), probabilities[6]]),
    )

    return get_forward([pp1, probabilities[2], pp2, probabilities[7], probabilities[9]])


def get_probability_schema_5(probabilities: list[float | int]) -> int | float:
    pp1 = get_parallel(get_parallel(probabilities[0], probabilities[1]), probabilities[6])
    pp2 = get_parallel(
        get_forward([probabilities[3], probabilities[4]]),
        get_forward([get_parallel(probabilities[5], probabilities[8]), probabilities[6]]),
    )

    return get_forward([pp1, pp2, probabilities[2], probabilities[7], probabilities[9]])


def get_probability_schema_6(probabilities: list[float | int]) -> int | float:
    pp1 = get_parallel(probabilities[0], probabilities[1])
    pp2 = get_parallel(
        get_forward([probabilities[3], probabilities[4]]), get_parallel(probabilities[5], probabilities[7])
    )
    pp3 = get_parallel(probabilities[9], probabilities[8])

    return get_forward([pp1, probabilities[2], pp2, probabilities[6], pp3])


def get_probability_schema_7(probabilities: list[float | int]) -> int | float:
    pp1 = get_parallel(probabilities[0], probabilities[1])
    pp2 = get_parallel(probabilities[2], get_parallel(probabilities[3], probabilities[4]))
    pp3 = get_parallel(
        get_parallel(probabilities[5], probabilities[6]), get_parallel(probabilities[7], probabilities[8])
    )

    return get_forward([pp1, pp2, pp3, probabilities[9]])


def get_probability_schema_8(probabilities: list[float | int]) -> int | float:
    ...


def get_probability_schema_9(probabilities: list[float | int]) -> int | float:
    pp1 = get_parallel(probabilities[0], probabilities[1])
    pp2 = get_parallel(pp1, get_forward([probabilities[2], probabilities[3]]))
    pp3 = get_parallel(
        get_parallel(get_parallel(probabilities[4], probabilities[5]), probabilities[6]), probabilities[7]
    )

    return get_forward([pp2, pp3, get_parallel(probabilities[8], probabilities[9])])


def get_probability_schema_10(probabilities: list[float | int]) -> int | float:
    pp1 = get_parallel(
        get_parallel(get_parallel(probabilities[0], probabilities[1]), probabilities[2]), probabilities[3]
    )
    pp2 = get_parallel(probabilities[6], probabilities[7])
    pp3 = get_parallel(pp2, get_forward([probabilities[8], probabilities[9]]))

    return get_forward([pp1, pp3, get_parallel(probabilities[5], probabilities[6])])


def get_probability_schema_11(probabilities: list[float | int]) -> int | float:
    pp1 = get_parallel(probabilities[0], get_forward([probabilities[1], probabilities[2]]))
    pp2 = get_parallel(get_parallel(probabilities[3], probabilities[4]), probabilities[5])
    pp3 = get_parallel(probabilities[6], probabilities[7])

    return get_forward([pp1, pp2, pp3, probabilities[8], probabilities[9]])


def get_probability_schema_12(probabilities: list[float | int]) -> int | float:
    pp1 = get_parallel(
        get_forward(
            [
                get_parallel(probabilities[0], probabilities[1]),
                get_parallel(get_parallel(probabilities[2], probabilities[3]), probabilities[4]),
            ]
        ),
        probabilities[5],
    )
    pp2 = get_parallel(get_parallel(probabilities[6], probabilities[7]), probabilities[7])

    return get_forward((pp1, pp2, probabilities[9]))


def get_probability_schema_13(probabilities: list[float | int]) -> int | float:
    pp1 = get_parallel(
        get_forward(
            (
                get_parallel(probabilities[0], probabilities[1]),
                get_parallel(get_parallel(probabilities[2], probabilities[3]), probabilities[4]),
            )
        ),
        probabilities[5],
    )
    pp2 = get_parallel(probabilities[7], probabilities[8])
    pp3 = get_parallel(probabilities[8], probabilities[9])

    return get_forward([pp1, pp2, pp3])


def get_probability_schema_14(probabilities: list[float | int]) -> int | float:
    pp1 = get_parallel(
        probabilities[9],
        get_forward(
            [
                get_parallel(probabilities[1], probabilities[2]),
                get_parallel(
                    get_forward([probabilities[3], probabilities[4], probabilities[5]]),
                    get_forward([get_parallel(probabilities[6], probabilities[7]), probabilities[9]]),
                ),
            ]
        ),
    )
    return get_forward([probabilities[0], pp1])


def get_probability_schema_15(probabilities: list[float | int]) -> int | float:
    pp1 = get_parallel(get_parallel(probabilities[1], probabilities[2]), probabilities[3])

    pp2 = get_parallel(get_parallel(probabilities[4], probabilities[5]), probabilities[6])
    pp3 = get_parallel(get_parallel(probabilities[7], probabilities[8]), pp2)

    return get_forward([probabilities[0], pp1, pp3, probabilities[9]])


def get_probability_schema_16(probabilities: list[float | int]) -> int | float:
    pp1 = get_parallel(probabilities[4], probabilities[5])
    pp2 = get_parallel(
        get_forward([get_parallel(probabilities[4], probabilities[5]), probabilities[8]]),
        get_forward([probabilities[3], probabilities[4], probabilities[5]]),
    )

    pp3 = get_parallel(get_forward([pp1, pp2]), probabilities[0])
    return get_forward([pp3, probabilities[9]])


def get_probability_schema_17(probabilities: list[float | int]) -> int | float:
    pp1 = get_parallel(probabilities[0], probabilities[1])

    pf1 = get_forward(
        (
            probabilities[2],
            probabilities[5],
            get_parallel(get_parallel(probabilities[4], probabilities[6]), probabilities[7]),
        )
    )
    pp2 = get_parallel(pf1, probabilities[4])

    pp3 = get_parallel(probabilities[8], probabilities[9])

    return get_forward([pp1, pp2, pp3])


def get_probability_schema_18(probabilities: list[float | int]) -> int | float:
    pp1 = get_parallel(probabilities[0], probabilities[1])
    pf1 = get_forward(
        [probabilities[2], get_parallel(get_parallel(probabilities[4], probabilities[6]), probabilities[7])]
    )
    pp2 = get_parallel(pf1, get_forward([probabilities[3], probabilities[5]]))
    pp3 = get_parallel(probabilities[8], probabilities[9])

    return get_forward([pp1, pp2, pp3])


def get_probability_schema_19(probabilities: list[float | int]) -> int | float:
    pp1 = get_parallel(probabilities[0], probabilities[1])
    pf1 = get_forward(
        [probabilities[2], get_parallel(get_parallel(probabilities[5], probabilities[6]), probabilities[7])]
    )
    pp2 = get_parallel(pf1, get_forward([probabilities[3], probabilities[4]]))
    pp3 = get_parallel(probabilities[8], probabilities[9])

    return get_forward([pp1, pp2, pp3])


def get_probability_schema_20(probabilities: list[float | int]) -> int | float:
    pp1 = get_parallel(probabilities[0], probabilities[1])
    pp2 = get_parallel(probabilities[4], get_forward([probabilities[2], probabilities[3]]))
    pp3 = get_parallel(probabilities[5], get_forward([pp1, pp2]))

    pp4 = get_parallel(
        get_parallel(probabilities[6], probabilities[7]), get_parallel(probabilities[8], probabilities[9])
    )

    return get_forward([pp3, pp4])


def get_probability_schema_21(probabilities: list[float | int]) -> int | float:
    # то же самое что и 3
    pass
    pp1 = get_parallel(probabilities[0], get_forward(probabilities[1:4]))
    pp2 = get_parallel(probabilities[4], get_parallel(probabilities[5], probabilities[6]))
    pf1 = get_forward([pp2, get_parallel(probabilities[8], probabilities[9])])
    pp3 = get_parallel(probabilities[8], pf1)

    return get_forward((pp1, pp3))


SCHEMAS = {
    1: get_probability_schema_1,
    2: get_probability_schema_2,
    3: get_probability_schema_3,
    4: get_probability_schema_4,
    5: get_probability_schema_5,
    6: get_probability_schema_6,
    7: get_probability_schema_7,
    # 8: get_probability_schema_8,
    9: get_probability_schema_9,
    10: get_probability_schema_10,
    11: get_probability_schema_11,
    12: get_probability_schema_12,
    13: get_probability_schema_13,
    14: get_probability_schema_14,
    15: get_probability_schema_15,
    16: get_probability_schema_16,
    17: get_probability_schema_17,
    18: get_probability_schema_18,
    19: get_probability_schema_19,
    20: get_probability_schema_20,
    21: get_probability_schema_21,
}
