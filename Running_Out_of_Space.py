# ====================== Running Out of Space ======================
def spacey(array):
    result = []
    space = ""
    for value in array:
        value_without_space = value.replace(" ", "")
        space += value_without_space
        result.append(space)
    return result

print(spacey(['kevin', ' has ','no','space']))
