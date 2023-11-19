import math

import lib.methods.third_lab.models as methods_third_lab_models
import lib.methods.third_lab.schemas as methods_third_lab_schemas


def get_rolling_reservation_probability(lambda_: float, m: int, t: float) -> float:
    p_probability = []
    for i in range(m):
        p_probability.append(pow(lambda_ * t, i) / math.factorial(i))

    return math.exp(-lambda_ * t) * sum(p_probability)


def calculate(request: methods_third_lab_models.ThirdLabModel):
    get_schema_probability = methods_third_lab_schemas.SCHEMAS.get(request.variant)
    if get_schema_probability is None:
        return "Нет решения для этого варианта"
    probabilities = []
    for lambda_, reserve in zip(
        (
            request.lambda_1,
            request.lambda_2,
            request.lambda_3,
            request.lambda_4,
            request.lambda_5,
            request.lambda_6,
            request.lambda_7,
            request.lambda_8,
            request.lambda_9,
            request.lambda_10,
        ),
        (
            request.reserve_1,
            request.reserve_2,
            request.reserve_3,
            request.reserve_4,
            request.reserve_5,
            request.reserve_6,
            request.reserve_7,
            request.reserve_8,
            request.reserve_9,
            request.reserve_10,
        ),
    ):
        probabilities.append(get_rolling_reservation_probability(lambda_, reserve, request.t))
    schema_probability = get_schema_probability(probabilities)
    response_text = f"{schema_probability} — вероятность безотказной работы."
    if schema_probability >= request.accuracy:
        response_text += " Точность достигнута."
    else:
        response_text += " Точность не достигнута."
    return response_text
