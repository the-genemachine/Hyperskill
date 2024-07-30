def check_values(value1, value2):
    return bool(value1) and bool(value2)


check_values(0, 1)  # False
check_values(1, 1)  # True
check_values(0, 0)  # False
check_values(1, 0)  # False
