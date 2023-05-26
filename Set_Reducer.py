# ==================== Set Reducer ====================
def set_reducer(inp):
    while len(inp) > 1:
        result = []
        i = 0
        while i < len(inp):
            count = 1
            while i + count < len(inp) and inp[i + count] == inp[i]:
                count += 1
            if count > 1:
                result.append(count)
            else:
                result.append(1)
            i += count
        inp = result
    return inp[0]
    
print(set_reducer([0, 4, 6, 8, 8, 8, 5, 5, 7])) # 2

# result = [1, 1, 1, 3, 2, 1] => [3, 1, 1, 1] => [1, 3] => [1, 1] => [2] => 2