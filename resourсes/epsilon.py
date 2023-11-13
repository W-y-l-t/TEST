def get_epsilon(expected_result, result):
    return abs(expected_result - result) / max(1, abs(result))
