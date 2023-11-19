import math

import lib.methods.third_lab.models as methods_third_lab_models
import lib.methods.third_lab.schemas as methods_third_lab_schemas


def get_permanent_reserve_probability(lambda_: float, m: int, t: float) -> float:
    return 1 - (1 - math.exp(-lambda_ * t)) ** m


def calculate(request: methods_third_lab_models.PermanentReserveModel):
    get_schema_probability = methods_third_lab_schemas.SCHEMAS.get(request.variant)
    if get_schema_probability is None:
        return "Нет решения для этого варианта"
    probabilities = []
    for lambda_ in (
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
    ):
        probabilities.append(get_permanent_reserve_probability(lambda_, request.reserve, request.t))
    schema_probability = get_schema_probability(probabilities)
    response_text = f"{schema_probability} — вероятность безотказной работы."
    if schema_probability >= request.accuracy:
        response_text += " Точность достигнута."
    else:
        response_text += " Точность не достигнута."
    return response_text
