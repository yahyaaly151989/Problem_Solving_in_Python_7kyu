# ======================= Length and Two Values =======================
def alternate(n, first_value, second_value):
    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append(first_value)
        else:
            result.append(second_value)
    return result

print(alternate(5, "true", "false"))