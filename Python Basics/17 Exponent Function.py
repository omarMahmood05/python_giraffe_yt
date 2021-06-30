def raise_to_power(base_num, power):
    result = 1
    for index in range(power):
        result = base_num * result
    return result

print(raise_to_power(9, 9))