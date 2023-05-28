# ==================== Find Duplicates ====================
def duplicates(arr):
    dict_counters = {}
    result = []
    for element in arr:
        if element not in dict_counters:
            dict_counters[element] = 1
        else:
            dict_counters[element] += 1
            if dict_counters[element] == 2 and element not in result:
                result.append(element)
    return result
    
    
print(duplicates([1, 2, 4, 4, 3, 3, 1, 5, 3, "5"]))